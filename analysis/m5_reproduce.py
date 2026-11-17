#!/usr/bin/env python3
"""IEEE Access Paper 2 M5 audit: label-exchangeable random-set null and 95% Wilson.
Inputs limited to mounted source entity CSV (no identifiers exported) plus documented WTMC aggregate.
The exact hypergeometric tail equals the permutation P-value for a fixed selected set
under exchangeability of exactly A attacker labels over N source entities.
"""
from pathlib import Path
import csv, math, json
import numpy as np
import pandas as pd
from scipy.stats import hypergeom
from statsmodels.stats.proportion import proportion_confint
from matplotlib import pyplot as plt
OUT=Path('/mnt/data/ieee_m5_work'); OUT.mkdir(parents=True,exist_ok=True)
SOURCES=[
    dict(dataset='WTMC2021',N=47,A=8,n=3,x=3,rule='P95 active-source',source='Full-graph original_kdis_clean aggregate, not a source-level CSV'),
    dict(dataset='NF-ToN-IoT-v2',file='/mnt/data/entity_table_NF-ToN-IoT-v2 (1).csv',threshold=214,rule='Admissible gap >=214',source='Complete labeled active-source entity table'),
    dict(dataset='NF-CSE-CIC-IDS2018-v2',file='/mnt/data/entity_table_NF-CSE-CIC-IDS2018-v2.csv',threshold=22,rule='P95 active-source >=22',source='Complete labeled active-source entity table'),
]
def interval(x,n):return proportion_confint(x,n,alpha=0.05,method='wilson')
rows=[]; curves=[]
for d in SOURCES:
    ds=d['dataset']
    if 'file' not in d:
        N,A,n,x=[d[t] for t in ('N','A','n','x')]
    else:
        inp=pd.read_csv(d['file'],usecols=['out_degree','src_is_attacker'])
        deg=inp.out_degree.to_numpy(dtype=np.int64); y=inp.src_is_attacker.to_numpy(dtype=np.int8)
        if np.any(deg<=0) or not np.isin(y,[0,1]).all():raise ValueError('Bad cohort')
        N=len(y);A=int(y.sum()); m=deg>=d['threshold'];n=int(m.sum());x=int(y[m].sum())
        idx=np.argsort(-deg,kind='stable'); deg=deg[idx]; y=y[idx]
        prefix=np.r_[0,np.cumsum(y,dtype=np.int64)]
        # Include every k=1..200, then spaced ranks out to n, without changing threshold selection.
        ks=sorted(set(list(range(1,min(200,N)+1)) + [k for k in (250,300,400,500,750,1000,1500,2000,3000,5000,10000,11571,20000) if k<=N] + [n]))
        for k in ks:
            edge=int(deg[k-1]);L=int(np.searchsorted(-deg,-edge,'left'));R=int(np.searchsorted(-deg,-edge,'right'))
            take=k-L; above=int(prefix[L]); tieA=int(prefix[R]-prefix[L]); tieN=R-L
            xlo=above+max(0,take-(tieN-tieA));xhi=above+min(take,tieA)
            if xlo>xhi:raise AssertionError('Tie bounds invalid')
            curves.append(dict(dataset=ds,k=k,degree_boundary=edge,tied_sources=tieN,
                               selected_from_ties=take,TP_min=xlo,TP_max=xhi,
                               precision_min=xlo/k,precision_max=xhi/k,
                               attacker_base_rate=A/N,
                               deterministic_rank_TP=int(prefix[k]),
                               note='Tie-safe bounds; deterministic rank is not a policy selection'))
    pl,ph=interval(x,n);rl,rh=interval(x,A)
    # Exact permutation p = hypergeom survival for at least observed TP.
    logp=float(hypergeom.logsf(x-1,N,A,n));p=math.exp(logp) if logp>-744 else 0.0
    rows.append(dict(dataset=ds,rule=d['rule'],N_active_sources=N,attacker_sources=A,base_rate=A/N,
        selected=n,selected_attackers=x,selected_nonattackers=n-x,
        selected_fraction=n/N,precision=x/n,precision_wilson_95_low=pl,precision_wilson_95_high=ph,
        recall=x/A,recall_wilson_95_low=rl,recall_wilson_95_high=rh,
        lift_vs_random_base=(x/n)/(A/N),
        random_set_expected_attackers=n*A/N,
        exact_random_set_p_ge_observed=p,exact_random_set_log10p=logp/math.log(10),
        expected_null='Hypergeometric N,A,n; attacker labels exchangeable at source level',
        provenance=d['source']))
    print(ds, 'N,A,n,TP',N,A,n,x,'P',x/n,'CI',pl,ph,'R',x/A,'R-CI',rl,rh,'expected',n*A/N,'p',p,'log10p',logp/math.log(10))

pd.DataFrame(rows).to_csv(OUT/'M5_Operating_Point_Wilson_ExactNull.csv',index=False)
cr=pd.DataFrame(curves); cr.to_csv(OUT/'M5_TieAware_PrecisionAtK.csv',index=False)
for ds,name in [('NF-ToN-IoT-v2','M5_PrecisionAtK_ToN.png'),('NF-CSE-CIC-IDS2018-v2','M5_PrecisionAtK_CSE.png')]:
    g=cr[(cr.dataset==ds)&(cr.k<=200)]
    fig,ax=plt.subplots(figsize=(5.6,3.25),dpi=220)
    xvals=g.k.to_numpy(); a=g.precision_min.to_numpy();b=g.precision_max.to_numpy()
    ax.plot(xvals,(a+b)/2,linewidth=1.9,label='Precision@k (tie-safe midpoint)')
    ax.fill_between(xvals,a,b,alpha=.15,label='Tied-degree admissible range')
    ax.axhline(float(g.attacker_base_rate.iloc[0]),linewidth=1.1,linestyle='--',label='Random-set expected precision')
    chosen=next(r for r in rows if r['dataset']==ds)
    if chosen['selected']<=200:ax.axvline(chosen['selected'],linewidth=1,linestyle=':',label=f"Policy set n={chosen['selected']:,}")
    ax.set_xlim(1,200);ax.set_ylim(0,1.04 if ds=='NF-ToN-IoT-v2' else 0.22)
    ax.set_xlabel('Top-k source entities (out-degree rank)')
    ax.set_ylabel('Retrospective Precision@k')
    ax.set_title(ds+' — rank sensitivity, not policy performance',fontsize=9.5)
    ax.grid(alpha=.22);ax.legend(loc='best',fontsize=6.2,frameon=False)
    fig.tight_layout();fig.savefig(OUT/name,bbox_inches='tight');plt.close(fig)
with open(OUT/'M5_Audit_Configuration.json','w') as f:
 json.dump(dict(method='95% Wilson for precision TP/n and recall TP/A',null='Exact hypergeometric random-set test conditional on N,A,n (random labels over entities)',curve='Top-k rank sensitivity for k=1..200 plus diagnostics; tie-safe extrema; no attacker labels influence sorting',wtmc_curve='NOT AVAILABLE; 47 active-source degree-label pairs absent',random_seed=None,no_monte_carlo=True,
                caveats=['Wilson intervals treat source entities as independent; duplicate hosts, temporal dependence and label provenance can invalidate nominal frequentist coverage','Random-set null is label exchangeability, not counterfactual impact of topology or PI; nonrandom labels by design','Rank-matched curves are retrospective diagnostics not Algorithm 1 operative sets','No production reputation data included because reference population not fully labeled']),f,indent=2)

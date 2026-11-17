"""M4: one-factor-at-a-time sensitivity on original active-source entity tables.
WARNING: DEVELOPMENT environments, NOT independent validation.
No IP/source identifier is printed or exported. Labels are used ONLY after topology decision.
"""
from pathlib import Path
import csv
import numpy as np

ROOT = Path('/mnt/data') if Path('/mnt/data/entity_table_NF-CSE-CIC-IDS2018-v2.csv').is_file() else Path('/content/drive/MyDrive/paper2_gsd_results')
DATASETS = {
    'NF-ToN-IoT-v2':'entity_table_NF-ToN-IoT-v2 (1).csv',
    'NF-CSE-CIC-IDS2018-v2':'entity_table_NF-CSE-CIC-IDS2018-v2.csv'
}
BASE = dict(delta_tc=0.05, mgr_low=2.0, mgr_high=5.0, gamma=3.0, k_min=2, top_k=30)
VARIANTS = {
    'delta_tc':[0.01,0.03,0.05,0.10],
    'mgr_low':[1.5,2.0,2.5],
    'mgr_high':[4.0,5.0,7.0],
    'gamma':[2.0,3.0,4.0,5.0],
    'k_min':[2,3,5,12],
    'top_k':[10,20,30,50]
}

def load(path):
    d,y=[],[]
    with open(path,encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            d.append(int(row['out_degree']))
            y.append(int(row['src_is_attacker']))
    x=np.array(d,dtype=np.int64)
    lab=np.array(y,dtype=np.int8)
    if np.any(x<=0): raise ValueError('Expected positive-degree active sources only')
    return x,lab

def prep(x):
    p90,p95,p97=np.percentile(x,[90,95,97],method='linear')
    top=np.sort(x[x>1])[::-1]
    return p90,p95,p97,top

def decide(x,p,**a):
    p90,p95,p97,top=p
    tc=bool(abs(p97-p90)/max(p97,1) < a['delta_tc'])
    window=top[:a['top_k']]
    ratios=window[:-1]/window[1:] if len(window)>1 else np.array([])
    mgr=float(np.max(ratios)) if len(ratios) else float('nan')
    valid=[]
    for i,r in enumerate(ratios,1):
        if r>a['gamma'] and i>=a['k_min']:
            valid.append((i,float(window[i-1])))
    tau=None;rank=None
    if not np.isfinite(mgr):
        state='INCONCLUSIVE_INSUFFICIENT_TAIL'
    elif mgr < a['mgr_low']:
        state='WEAK_ISOLATION'
    elif mgr < a['mgr_high']:
        state='INCONCLUSIVE_BAND'
    elif not tc:
        tau=p95
        state='STRONG_CANDIDATE_P95'
    elif valid:
        rank,tau=valid[0]
        state='STRONG_CANDIDATE_GAP'
    else:
        state='INCONCLUSIVE_NO_ADMISSIBLE_GAP'
    mask=(x>=tau) if tau is not None else np.zeros(x.size,dtype=bool)
    if state.startswith('STRONG') and (not mask.any() or mask.all()):
        state='INCONCLUSIVE_EMPTY_OR_SATURATED';mask=np.zeros(x.size,dtype=bool);tau=None
    return dict(state=state,TC=tc,MGR=round(mgr,8),threshold=tau,gap_rank=rank,selected=int(mask.sum()),mask=mask)

def main():
    rows=[]
    for name,path in DATASETS.items():
        x,y=load(ROOT/path)
        prepared=prep(x)
        for param,values in [('baseline',[BASE.get('delta_tc')])] + list(VARIANTS.items()):
            # Special baseline independent of parameter axes
            if param=='baseline':
                values=['baseline']
            for value in values:
                params=dict(BASE)
                if param!='baseline':params[param]=value
                z=decide(x,prepared,**params)
                selected=z.pop('mask')
                tp=int(np.sum(y[selected]))
                n=z['selected']; attackers=int(y.sum())
                row=dict(environment=name,parameter=param,value=value,
                    n_active=len(x),n_attackers=attackers,
                    **z,
                    TP=tp,FP=n-tp,
                    precision=tp/n if n else None,
                    recall=tp/attackers if attackers and n else None)
                rows.append(row)
                print(name,param,value,row['state'],'selected',n,'precision',row['precision'])
    path=ROOT/'IEEE_Access_M4_Sensitivity_OAT.csv'
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print('Saved',path)

if __name__=='__main__':main()

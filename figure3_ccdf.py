"""
Figure 3 — Source Out-Degree CCDF Comparison
NF-ToN-IoT-v2 (Case I) vs NF-CSE-CIC-IDS2018-v2 (Case II)

Usage: Run in Google Colab or locally.
Requires: entity_table_ALL.csv in the same directory.
Output: Figure3_CCDF_comparison.pdf / .png (300 dpi, publication-ready)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# ── Load data ──────────────────────────────────────────────────────────────────
df = pd.read_csv('entity_table_ALL.csv')

# ── Layout ─────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
fig.patch.set_facecolor('white')

CONFIGS = [
    {
        'dataset':   'NF-ToN-IoT-v2',
        'ax':        axes[0],
        'title':     '(a)  NF-ToN-IoT-v2\nCase I — High GSD, High PI',
        'line_col':  '#1a6b3c',
        'note':      '99% of entities at\nout-degree = 1',
        'note_xy':   (0.58, 0.72),
        'pi_label':  'Attacker entities clearly isolated\nin extreme structural tail',
        'pi_xy':     (0.30, 0.18),
        'panel':     'A',
    },
    {
        'dataset':   'NF-CSE-CIC-IDS2018-v2',
        'ax':        axes[1],
        'title':     '(b)  NF-CSE-CIC-IDS2018-v2\nCase II — High GSD, Low PI',
        'line_col':  '#1d6fa4',
        'note':      'Benign infrastructure\nout-degree up to 2,525',
        'note_xy':   (0.42, 0.65),
        'pi_label':  'Attacker entities indistinguishable\nfrom benign infrastructure',
        'pi_xy':     (0.28, 0.18),
        'panel':     'B',
    },
]

for cfg in CONFIGS:
    ax  = cfg['ax']
    sub = df[df['source_dataset'] == cfg['dataset']].copy()
    n   = len(sub)

    # ── CCDF (all entities) ────────────────────────────────────────────────────
    all_deg    = np.sort(sub['out_degree'].values)[::-1]
    ccdf_y     = np.arange(1, n + 1) / n
    ax.loglog(all_deg, ccdf_y,
              color=cfg['line_col'], linewidth=1.6, alpha=0.85, zorder=2,
              label='All entities (CCDF)')

    # ── Attacker markers ───────────────────────────────────────────────────────
    atk = sub[sub['src_is_attacker'] == 1].copy()
    for _, row in atk.iterrows():
        y_val = np.sum(sub['out_degree'] >= row['out_degree']) / n
        ax.scatter(row['out_degree'], y_val,
                   color='#e63946', s=55, zorder=5,
                   marker='x', linewidths=2.0)

    # ── Top benign markers (NF-CSE only, to show infrastructure overlap) ───────
    if cfg['dataset'] == 'NF-CSE-CIC-IDS2018-v2':
        top_benign = sub[sub['src_is_attacker'] == 0].nlargest(15, 'out_degree')
        for _, row in top_benign.iterrows():
            y_val = np.sum(sub['out_degree'] >= row['out_degree']) / n
            ax.scatter(row['out_degree'], y_val,
                       color='#f4a261', s=40, zorder=4,
                       marker='o', linewidths=1.0,
                       facecolors='none', edgecolors='#f4a261')

    # ── P95 threshold line ────────────────────────────────────────────────────
    p95 = np.percentile(sub['out_degree'], 95)
    ax.axvline(x=max(p95, 1.1), color='#888', linestyle='--',
               linewidth=1.0, alpha=0.7, zorder=1)
    ax.text(max(p95, 1.1) * 1.15, ccdf_y[int(n * 0.10)],
            f'P95 = {p95:.0f}',
            fontsize=9, color='#666', va='center', ha='left')

    # ── Annotation boxes ──────────────────────────────────────────────────────
    ax.text(*cfg['note_xy'], cfg['note'],
            transform=ax.transAxes, fontsize=9.5, color='#444',
            va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f9f9f9',
                      edgecolor='#ccc', alpha=0.9))

    ax.text(*cfg['pi_xy'], cfg['pi_label'],
            transform=ax.transAxes, fontsize=9.5,
            color='#e63946' if 'isolated' in cfg['pi_label'] else '#c45c11',
            va='bottom', ha='left', style='italic')

    # ── Axes formatting ───────────────────────────────────────────────────────
    ax.set_xlabel('Source out-degree (log scale)', fontsize=11)
    ax.set_ylabel('P(Degree ≥ x)', fontsize=11)
    ax.set_title(cfg['title'], fontsize=11.5, fontweight='bold', pad=10)
    ax.grid(True, which='both', linestyle='--', alpha=0.3, color='#aaa')
    ax.set_facecolor('white')
    ax.spines[['top', 'right']].set_visible(False)

# ── Shared legend ──────────────────────────────────────────────────────────────
atk_marker  = mlines.Line2D([], [], color='#e63946', marker='x',
                              linestyle='None', markersize=8,
                              markeredgewidth=2, label='Attacker entity')
infra_marker = mlines.Line2D([], [], color='#f4a261', marker='o',
                               linestyle='None', markersize=8,
                               markeredgewidth=1.5, fillstyle='none',
                               label='Benign infrastructure (top 15)')
ccdf_line    = mlines.Line2D([], [], color='#555', linewidth=1.5,
                              label='Full entity CCDF')

axes[1].legend(handles=[ccdf_line, atk_marker, infra_marker],
               fontsize=9.5, loc='lower left',
               framealpha=0.9, edgecolor='#ccc')

# ── Save ───────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=2.5, w_pad=3.0)
plt.savefig('Figure3_CCDF_comparison.pdf', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.savefig('Figure3_CCDF_comparison.png', dpi=300,
            bbox_inches='tight', facecolor='white')
print("Saved: Figure3_CCDF_comparison.pdf / .png")
plt.show()

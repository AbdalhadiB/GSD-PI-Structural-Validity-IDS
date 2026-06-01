"""
figure3_ccdf_updated.py
Updated Figure 3: Source out-degree CCDF for NF-ToN-IoT-v2 (Case II) 
and NF-CSE-CIC-IDS2018-v2 (Case III)

Updated labels to match four-case taxonomy:
  Case I   — Full Structural Utility       (WTMC2021)
  Case II  — Recoverable Structural Utility (NF-ToN-IoT-v2)
  Case III — No Structural Utility          (NF-CSE-CIC-IDS2018-v2)
  Case IV  — Degenerate Structural Utility  (UNSW-NB15, NF-UNSW-NB15-v2)

Usage (Colab):
  1. Upload entity_table_ALL.csv to /content/ or adjust DATA_PATH
  2. Run: python figure3_ccdf_updated.py
  3. Output: figure3_ccdf.png (300 DPI, journal-ready)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import pandas as pd
from pathlib import Path

# ── Configuration ────────────────────────────────────────────
DATA_PATH   = "entity_table_ALL.csv"   # adjust if needed
OUTPUT_PATH = "figure3_ccdf.png"
DPI         = 300
TOP_BENIGN  = 15   # number of top benign infrastructure entities to highlight

# ── Load data ────────────────────────────────────────────────
df_all = pd.read_csv(DATA_PATH)
df_ton  = df_all[df_all['source_dataset'] == 'NF-ToN-IoT-v2'].copy()
df_cic  = df_all[df_all['source_dataset'] == 'NF-CSE-CIC-IDS2018-v2'].copy()

print(f"NF-ToN-IoT-v2:        {len(df_ton):,} entities, "
      f"{df_ton['src_is_attacker'].sum():,} attackers")
print(f"NF-CSE-CIC-IDS2018-v2: {len(df_cic):,} entities, "
      f"{df_cic['src_is_attacker'].sum():,} attackers")

# ── CCDF helper ──────────────────────────────────────────────
def compute_ccdf(out_degrees):
    od_sorted = np.sort(out_degrees)
    n = len(od_sorted)
    ccdf = 1.0 - np.arange(n) / n
    return od_sorted, ccdf

def p95(out_degrees):
    return float(np.percentile(out_degrees, 95))

# ── Figure setup ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.patch.set_facecolor('white')

CCDF_COLOR_TON  = '#1a6b2e'   # dark green for ToN-IoT
CCDF_COLOR_CIC  = '#1a3a6b'   # dark blue for CIC-IDS2018
ATTACKER_COLOR  = '#cc0000'   # red X for attackers
BENIGN_COLOR    = '#e07b00'   # orange circle for benign infra
THRESH_COLOR    = '#555555'   # grey dashed threshold line
ANNOT_COLOR     = '#cc0000'   # annotation text color (attacker)
ANNOT_COLOR_B   = '#e07b00'   # annotation text color (benign)
ANNOT_COLOR_G   = '#1a6b2e'   # annotation text color (general)

# ─────────────────────────────────────────────────────────────
# Panel (a): NF-ToN-IoT-v2
# Case II — Recoverable Structural Utility
# ─────────────────────────────────────────────────────────────
ax = axes[0]
ax.set_facecolor('#f8f8f8')

od_ton   = df_ton['out_degree'].values.astype(float)
att_ton  = df_ton[df_ton['src_is_attacker'] == 1]['out_degree'].values.astype(float)
x_t, y_t = compute_ccdf(od_ton)

# CCDF line
ax.step(x_t, y_t, where='post', color=CCDF_COLOR_TON,
        linewidth=1.5, alpha=0.9, label='Full entity CCDF')

# P95 threshold line
p95_ton = p95(od_ton)
ax.axvline(x=p95_ton, color=THRESH_COLOR, linestyle='--',
           linewidth=1.0, alpha=0.7)
ax.text(p95_ton * 1.15, 0.65, f'P95 = {int(p95_ton)}',
        color=THRESH_COLOR, fontsize=9, fontstyle='italic')

# Attacker entities
for od in att_ton:
    _, ccdf_val = compute_ccdf(od_ton)
    idx = np.searchsorted(x_t, od)
    y_val = y_t[min(idx, len(y_t)-1)]
    ax.scatter(od, y_val, marker='x', color=ATTACKER_COLOR,
               s=60, linewidths=1.8, zorder=5)

# Annotations
ax.annotate('99% of entities at\nout-degree = 1',
            xy=(1.05, 0.58), xytext=(2.5, 0.25),
            fontsize=8.5, color='#333333',
            bbox=dict(boxstyle='round,pad=0.3', fc='white',
                      ec='#aaaaaa', alpha=0.85),
            arrowprops=dict(arrowstyle='->', color='#666666', lw=0.8))

ax.text(80, 5e-4,
        'Attacker entities clearly isolated\nin extreme structural tail',
        fontsize=8.5, color=ANNOT_COLOR, fontstyle='italic',
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.25', fc='white',
                  ec=ATTACKER_COLOR, alpha=0.7, lw=0.6))

# Formatting
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Source out-degree (log scale)', fontsize=10)
ax.set_ylabel(r'P(Degree $\geq$ x)', fontsize=10)
ax.set_title('(a)  NF-ToN-IoT-v2\n'
             'Case II \u2014 Recoverable Structural Utility\n'
             '(Population-Expansion TC, High PI)',
             fontsize=10.5, fontweight='bold', pad=10,
             linespacing=1.4)
ax.grid(True, which='both', linestyle=':', linewidth=0.4,
        color='#cccccc', alpha=0.8)
ax.set_xlim(left=0.8)
ax.tick_params(labelsize=9)

# ─────────────────────────────────────────────────────────────
# Panel (b): NF-CSE-CIC-IDS2018-v2
# Case III — No Structural Utility
# ─────────────────────────────────────────────────────────────
ax = axes[1]
ax.set_facecolor('#f8f8f8')

od_cic  = df_cic['out_degree'].values.astype(float)
att_cic = df_cic[df_cic['src_is_attacker'] == 1]['out_degree'].values.astype(float)
x_c, y_c = compute_ccdf(od_cic)

# Top benign infrastructure entities
benign_cic = (df_cic[df_cic['src_is_attacker'] == 0]
              .nlargest(TOP_BENIGN, 'out_degree')['out_degree'].values.astype(float))

# CCDF line
ax.step(x_c, y_c, where='post', color=CCDF_COLOR_CIC,
        linewidth=1.5, alpha=0.9, label='Full entity CCDF')

# P95 threshold line
p95_cic = p95(od_cic)
ax.axvline(x=p95_cic, color=THRESH_COLOR, linestyle='--',
           linewidth=1.0, alpha=0.7)
ax.text(p95_cic * 1.12, 0.4, f'P95 = {int(p95_cic)}',
        color=THRESH_COLOR, fontsize=9, fontstyle='italic')

# Attacker entities
for od in att_cic:
    idx = np.searchsorted(x_c, od)
    y_val = y_c[min(idx, len(y_c)-1)]
    ax.scatter(od, y_val, marker='x', color=ATTACKER_COLOR,
               s=60, linewidths=1.8, zorder=5, label='_nolegend_')

# Benign infrastructure entities
for od in benign_cic:
    idx = np.searchsorted(x_c, od)
    y_val = y_c[min(idx, len(y_c)-1)]
    ax.scatter(od, y_val, marker='o', color=BENIGN_COLOR,
               s=50, zorder=5, alpha=0.85, label='_nolegend_')

# Max benign out-degree annotation
max_benign = int(benign_cic.max())
ax.annotate(f'Benign infrastructure\nout-degree to {max_benign:,}',
            xy=(max_benign, y_c[np.searchsorted(x_c, max_benign)]),
            xytext=(max_benign * 0.3, 5e-4),
            fontsize=8.5, color=ANNOT_COLOR_B, fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color=BENIGN_COLOR, lw=0.8))

ax.text(200, 1e-4,
        'Attacker entities indistinguishable\nfrom benign infrastructure',
        fontsize=8.5, color=ANNOT_COLOR, fontstyle='italic',
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.25', fc='white',
                  ec=ATTACKER_COLOR, alpha=0.7, lw=0.6))

# Formatting
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Source out-degree (log scale)', fontsize=10)
ax.set_ylabel(r'P(Degree $\geq$ x)', fontsize=10)
ax.set_title('(b)  NF-CSE-CIC-IDS2018-v2\n'
             'Case III \u2014 No Structural Utility\n'
             '(High GSD, Low PI)',
             fontsize=10.5, fontweight='bold', pad=10,
             linespacing=1.4)
ax.grid(True, which='both', linestyle=':', linewidth=0.4,
        color='#cccccc', alpha=0.8)
ax.set_xlim(left=0.8)
ax.tick_params(labelsize=9)

# ── Shared legend ─────────────────────────────────────────────
legend_elements = [
    Line2D([0], [0], color=CCDF_COLOR_TON,  linewidth=1.5,
           label='Full entity CCDF (NF-ToN-IoT-v2)'),
    Line2D([0], [0], color=CCDF_COLOR_CIC,  linewidth=1.5,
           label='Full entity CCDF (NF-CSE-CIC-IDS2018-v2)'),
    Line2D([0], [0], marker='x', color=ATTACKER_COLOR,
           linewidth=0, markersize=7, markeredgewidth=1.8,
           label='Attacker entity'),
    Line2D([0], [0], marker='o', color=BENIGN_COLOR,
           linewidth=0, markersize=6, alpha=0.85,
           label=f'Benign infrastructure (top {TOP_BENIGN})'),
]

fig.legend(handles=legend_elements,
           loc='lower center', ncol=2,
           fontsize=8.5, framealpha=0.9,
           edgecolor='#cccccc',
           bbox_to_anchor=(0.5, -0.08))

# ── Caption ──────────────────────────────────────────────────
caption = (
    "Figure 3.  Source out-degree complementary cumulative distribution functions (CCDF) for "
    "NF-ToN-IoT-v2 (Case II, Recoverable Structural Utility, High PI)\n"
    "and NF-CSE-CIC-IDS2018-v2 (Case III, No Structural Utility, Low PI). "
    "Attacker entities (\u00d7) are structurally isolated in the extreme tail in NF-ToN-IoT-v2,\n"
    "whereas in NF-CSE-CIC-IDS2018-v2 they are indistinguishable from benign high-connectivity "
    "infrastructure (\u25cb). The contrast operationalizes the PI condition empirically."
)
fig.text(0.5, -0.17, caption, ha='center', va='top',
         fontsize=9, fontstyle='italic', color='#222222',
         wrap=True, multialignment='center')

plt.tight_layout(rect=[0, 0.02, 1, 1])
plt.savefig(OUTPUT_PATH, dpi=DPI, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print(f"\nSaved: {OUTPUT_PATH}  ({DPI} DPI)")
plt.close()

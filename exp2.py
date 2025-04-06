import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_multi = pd.read_csv('resistencias_serie_multi.csv')
df_multi.columns = [col.strip().lower().replace(" ", "_") for col in df_multi.columns]

resistencias_mom = df_multi["mom"]
error_absoluto_individual = 0.05  # 5% de 1 MΩ
x_pos = np.arange(len(resistencias_mom))

fig, ax = plt.subplots(figsize=(8, 6))
ax.errorbar(x_pos, resistencias_mom, yerr=error_absoluto_individual, fmt='o', capsize=6, linestyle='None', color='blue')
ax.set_xticks(x_pos)
ax.set_xticklabels([f"R{i+1}" for i in x_pos])
ax.set_ylabel('Resistencia [MΩ]')
ax.set_title('Medición individual de resistencias (multímetro)')

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
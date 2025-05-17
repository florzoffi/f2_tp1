import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer datos
data = pd.read_csv('serie_naranja.csv')
data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]

# Extraer variables
corriente_mA = data['ma']
voltaje = data['voltage']
corriente_A = corriente_mA / 1000

# Ajuste lineal
a, b = np.polyfit(corriente_A, voltaje, 1)
R_ajustada = a
R_multimetro = 9880
R_colorimetria = 10000

# Errores instrumentales para el ajuste lineal
V_mean = np.mean(voltaje)
I_mean = np.mean(corriente_A)

delta_V = np.sqrt((0.005 * V_mean + 0.02)**2 + (0.005 * V_mean + 0.01)**2)  # multímetro + fuente
delta_I = 0.01 * I_mean + 0.00002  # multímetro (1% + 0.02 mA → en A)
rel_error_R = np.sqrt((delta_V / V_mean)**2 + (delta_I / I_mean)**2)
error_ajuste = R_ajustada * rel_error_R

# Otros errores
error_colorimetrico = R_colorimetria * 0.05
error_multimetro = 6

# Armado de gráfico
labels = ['Valor Nominal', 'Multímetro', 'Ajuste lineal']
resistencias = [R_colorimetria, R_multimetro, R_ajustada]
errores = [error_colorimetrico, error_multimetro, error_ajuste]
x_pos = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(8, 6))
ax.errorbar(x_pos, resistencias, yerr=errores, fmt='o', capsize=10,
            linestyle='None', color='darkorange')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_ylabel('Resistencia [Ω]')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("grafico_comparacion_resistencias_naranja.png")
plt.show()

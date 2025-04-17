import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer datos
data_roja = pd.read_csv('serie_rojo.csv')
data_naranja = pd.read_csv('serie_naranja.csv')

# Normalizar nombres de columnas
for df in [data_roja, data_naranja]:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Extraer variables
I_roja = data_roja['ma'] / 1000
V_roja = data_roja['voltage']

I_naranja = data_naranja['ma'] / 1000
V_naranja = data_naranja['voltage']

# Ajustes lineales
a_r, b_r = np.polyfit(I_roja, V_roja, 1)
a_n, b_n = np.polyfit(I_naranja, V_naranja, 1)

# Rectas ajustadas
I_fit_r = np.linspace(min(I_roja), max(I_roja), 100)
V_fit_r = a_r * I_fit_r + b_r

I_fit_n = np.linspace(min(I_naranja), max(I_naranja), 100)
V_fit_n = a_n * I_fit_n + b_n

# ---------- GRAFICO PRINCIPAL CON DOS RECTAS ----------
fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True,
                       gridspec_kw={'height_ratios': [3, 1]})

# Gráfico superior: V vs I
axs[0].errorbar(I_roja, V_roja, yerr=0.07, fmt='o', capsize=4, label='Datos Serie Roja', color='red')
axs[0].plot(I_fit_r, V_fit_r, '-', color='darkred', label=f'Ajuste Roja: V = {a_r:.2f}·I + {b_r:.2f}')

axs[0].errorbar(I_naranja, V_naranja, yerr=0.07, fmt='s', capsize=4, label='Datos Serie Naranja', color='orange')
axs[0].plot(I_fit_n, V_fit_n, '-', color='darkorange', label=f'Ajuste Naranja: V = {a_n:.2f}·I + {b_n:.2f}')

axs[0].set_ylabel('Voltaje [V]')
axs[0].set_title('Comparación de Ley de Ohm: Resistencia Roja vs Naranja')
axs[0].legend()
axs[0].grid(True)

# Gráfico inferior: residuos
residuos_rojo = (V_roja - (a_r * I_roja + b_r)) / 0.07
residuos_naranja = (V_naranja - (a_n * I_naranja + b_n)) / 0.07

axs[1].axhline(0, color='gray', linestyle='--')
axs[1].scatter(I_roja, residuos_rojo, label='Residuos Roja', color='red')
axs[1].scatter(I_naranja, residuos_naranja, label='Residuos Naranja', color='orange')

axs[1].set_xlabel('Corriente [A]')
axs[1].set_ylabel('Residuo normalizado')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.savefig("comparacion_rectas_y_residuos.png")
plt.show()
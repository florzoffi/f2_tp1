import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_med = pd.read_csv('resistencias_serie_mediciones.csv')
df_med.columns = [col.strip().lower().replace(" ", "_") for col in df_med.columns]

df_med["corriente_a"] = df_med["ma"] / 1000
df_med["resistencia_calculada"] = df_med["voltage"] / df_med["corriente_a"]
df_med_valid = df_med[df_med["corriente_a"] > 0]

voltajes = df_med_valid["voltage"]
corrientes = df_med_valid["corriente_a"]

a, b = np.polyfit(corrientes, voltajes, 1)
I_fit = np.linspace(min(corrientes), max(corrientes), 100)
V_fit = a * I_fit + b

plt.figure(figsize=(8, 6))
plt.plot(corrientes, voltajes, 'o', label='Datos experimentales')
plt.plot(I_fit, V_fit, '-', label=f'Ajuste lineal: V = {a:.2f}·I + {b:.2f}')
plt.xlabel('Corriente [A]')
plt.ylabel('Voltaje [V]')
plt.title('Gráfico V vs I - Resistencia total del conjunto')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
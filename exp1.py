import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('fuente_multimetro.csv')
data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
data.rename(columns={'volataje_fuente': 'voltaje_fuente'}, inplace=True)
x = data['voltaje_fuente']
y = data['voltaje_multimetro']

a, b = np.polyfit(x, y, 1)
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * x_fit + b
error_sist_voltimetro = round(abs(b) + 0.01, 3) 

plt.figure(figsize=(8, 6))
plt.errorbar(x, y, yerr=error_sist_voltimetro, fmt='o', capsize=4, label='Datos experimentales ± error')
plt.plot(x_fit, y_fit, '-', label=f'Ajuste lineal: y = {a:.3f}x + {b:.3f}')
plt.xlabel('Voltaje fuente [V]')
plt.ylabel('Voltaje medido por multímetro [V]')
plt.title('Voltaje medido vs Voltaje fuente')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_fuente_vs_multimetro.png")
plt.show()

print(f"Pendiente (a): {a:.3f}")
print(f"Offset (b): {b:.3f}")
print(f"Error sistemático sugerido para barras de error en voltaje: ±{error_sist_voltimetro:.3f} V")
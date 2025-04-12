import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv( 'serie_rojo.csv' )
data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]

corriente_mA = data['ma']        
voltaje = data['voltage']        
corriente_A = corriente_mA / 1000

a, b = np.polyfit(corriente_A, voltaje, 1) 
error_y = 0.07  
I_fit = np.linspace(min(corriente_A), max(corriente_A), 100)
V_fit = a * I_fit + b

plt.figure(figsize=(8, 6))
plt.errorbar(corriente_A, voltaje, yerr=error_y, fmt='o', capsize=4, label='Datos experimentales')
plt.plot(I_fit, V_fit, '-', label=f'Ajuste lineal: V = {a:.2f}·I + {b:.2f}')
plt.xlabel('Corriente [A]')
plt.ylabel('Voltaje [V]')
plt.title('Validación de la Ley de Ohm - Resistencia Serie Roja')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_ley_ohm_rojo.png")
plt.show()

R_ajustada = a 
R_multimetro = 980 
R_colorimetria = 1000 

error_colorimetrico = R_colorimetria * 0.05 
error_abs = abs(R_ajustada - R_multimetro)

labels = ['Colorimetría', 'Multímetro', 'Ajuste lineal']
resistencias = [R_colorimetria, R_multimetro, R_ajustada]
errores = [error_colorimetrico, 6, error_abs] 
x_pos = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(8, 6))
ax.errorbar(x_pos, resistencias, yerr=errores, fmt='o', capsize=10,
            linestyle='None', color='darkred')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_ylabel('Resistencia [Ω]')
ax.set_title('Comparación de métodos de medición de resistencia')

plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("grafico_comparacion_resistencias_rojo.png") 
plt.show()
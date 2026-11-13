# Calculo del Indice de Masa Corporal (IMC)
# Definicion de variables
peso = 70 # Kilogramos
altura = 1.75 # en metros

# Calculo del IMC
imc = peso / (altura ** 2)
print(imc)

# Clasificacion del IMC
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9: # imc >= 18.5 and imc < 29.9
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
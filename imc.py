# Sprint 1 - Cálculo do IMC

# Solicitar dados ao utilizador
peso = float(input("Introduz o teu peso (kg): "))
altura_cm = float(input("Introduz a tua altura (cm): "))

# Converter altura para metros
altura_m = altura_cm / 100

# Calcular IMC
imc = peso / (altura_m * altura_m)

# Mostrar IMC arredondado
print(f"\nIMC calculado: {imc:.2f}")

# Classificação
if imc < 18.5:
    print("Fora do peso normal")
elif imc < 25:
    print("Peso normal")
else:
    print("Fora do peso normal")

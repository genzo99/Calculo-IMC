
def converter_altura(altura_cm: float) -> float:
    """Converte centímetros para metros."""
    return altura_cm / 100


def calcular_imc(peso: float, altura_m: float) -> float:
    """Calcula o IMC."""
    return peso / (altura_m * altura_m)


def classificar_imc(imc: float) -> str:
    """Classifica o IMC segundo a OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


def main():
    print("=== Cálculo do IMC ===\n")

    peso = float(input("Introduz o teu peso (kg): "))
    altura_cm = float(input("Introduz a tua altura (cm): "))

    altura_m = converter_altura(altura_cm)
    imc = calcular_imc(peso, altura_m)
    classificacao = classificar_imc(imc)

    print(f"\nIMC calculado: {imc:.2f}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()

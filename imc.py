

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


def pedir_float(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))

            if valor <= 0:
                print("⚠ Erro: o valor deve ser maior que zero.")
                continue

            return valor

        except ValueError:
            print("⚠ Erro: deves inserir um número válido.")


def mostrar_resumo(total, lista_imc, lista_classificacoes):
    """Mostra o resumo final das consultas."""
    if total == 0:
        print("\nNenhuma consulta foi realizada.")
        return

    media_imc = sum(lista_imc) / total

    
    frequencias = {}
    for c in lista_classificacoes:
        frequencias[c] = frequencias.get(c, 0) + 1

    mais_frequente = max(frequencias, key=frequencias.get)

    print("\n===== RESUMO FINAL =====")
    print(f"Total de consultas: {total}")
    print(f"Média dos IMC: {media_imc:.2f}")
    print(f"Classificação mais frequente: {mais_frequente}")


def main():
    total_consultas = 0
    lista_imc = []
    lista_classificacoes = []

    while True:
        print("\n--- Nova Consulta IMC ---")

        peso = pedir_float("Introduz o peso (kg): ")
        altura_cm = pedir_float("Introduz a altura (cm): ")

        altura_m = converter_altura(altura_cm)
        imc = calcular_imc(peso, altura_m)
        classificacao = classificar_imc(imc)

        print(f"\nIMC calculado: {imc:.2f}")
        print(f"Classificação: {classificacao}")

        total_consultas += 1
        lista_imc.append(imc)
        lista_classificacoes.append(classificacao)

        continuar = input("\nQueres realizar outra consulta? (s/n): ").strip().lower()
        if continuar != "s":
            break

    mostrar_resumo(total_consultas, lista_imc, lista_classificacoes)
    print("\nPrograma terminado. Obrigado!")


if __name__ == "__main__":
    main()


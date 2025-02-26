def main():
    results = []
    while True:
        print("Digite os números que deseja somar, separados por espaço (ou 'sair' para finalizar):")
        user_input = input()
        if user_input.lower() == 'sair':
            break
        try:
            numbers = list(map(float, user_input.split()))
            result = sum(numbers)
            results.append(result)
            print(f"Resultado da soma: {result}")
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números separados por espaço.")
    
    print("\nResultados salvos:")
    for i, result in enumerate(results, 1):
        print(f"Resultado {i}: {result}")

if __name__ == "__main__":
    main()
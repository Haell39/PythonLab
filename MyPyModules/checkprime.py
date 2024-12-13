def is_prime(number):
    """Função para verificar se um número é primo."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    """Função principal para executar o verificador de primos."""
    while True:
        user_input = input("Digite um número para verificar se é primo (ou 'sair' para encerrar): ")

        if user_input.lower() == "sair":
            print("Saindo do programa. Até a próxima!")
            break

        try:
            num = int(user_input)
            if is_prime(num):
                print(f"{num} é um número primo!")
            else:
                print(f"{num} não é um número primo.")
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para encerrar!")


if __name__ == "__main__":
    main()
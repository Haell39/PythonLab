try:
    # Solicitando entrada do usuário
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))

    # Tentativa de divisão
    resultado = a / b

# Tratando entradas inválidas (não numéricas)
except ValueError:
    print("Erro: Você precisa digitar um número válido.")

# Tratando divisão por zero
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# Tratando qualquer outro tipo de erro não especificado
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

# Executado se nenhum erro ocorrer no bloco try
else:
    print(f'O resultado da divisão é: {resultado:.2f}')

# Executado independentemente de ocorrer um erro ou não
finally:
    print("Obrigado por usar o programa. Encerrando...")

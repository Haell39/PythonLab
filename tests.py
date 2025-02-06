import math

def calcular_logaritmo_natural(valor):
    """
    Calcula o logaritmo natural (base e) de um valor.
    
    :param valor: O valor para o qual calcular o logaritmo natural.
    :return: O logaritmo natural do valor.
    """
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    return math.log(valor)

# Exemplo de uso
if __name__ == "__main__":
    try:
        valor = float(input("Digite um número para calcular o logaritmo natural: "))
        print(f"O logaritmo natural de {valor} é {calcular_logaritmo_natural(valor)}")
    except ValueError as e:
        print(f"Erro: {e}")
        
        
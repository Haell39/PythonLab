# Programa que calcula o número de grãos de trigo em um tabuleiro de xadrez

def calcular_graos():
    graos = 1  # Começa com 1 grão no primeiro quadro
    total_graos = 0  # Total de grãos

    for i in range(1, 65):  # De 1 a 64
        total_graos += graos  # Acumula o total de grãos
        graos *= 2  # Dobra a quantidade de grãos a cada quadro

    return total_graos

if __name__ == "__main__":
    total = calcular_graos()
    print(f"Total de grãos de trigo a serem recebidos: {total}")
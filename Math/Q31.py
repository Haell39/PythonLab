
'''
Escrever um programa que leia um conjunto de números positivos, e exiba se o número lido é par ou ímpar. Exiba
ao final a soma total dos números pares lidos e também a soma dos números ímpares lidos. Suporemos que o
número de elementos deste conjunto não é conhecido, e que um número negativo será utilizado para sinalizar o fim
dos dados. 
'''

def main():
    pares = 0
    impares = 0

    numeros = input("Digite uma sequência de números separados por espaço (um número negativo encerra): ").split()

    for num_str in numeros:
        num = int(num_str)  #
        if num < 0:  # 
            break
        if num % 2 == 0:  # 
            pares += num
        else:  
            impares += num

    print("Soma dos números pares: ", pares)
    print("Soma dos números ímpares: ", impares)

main()

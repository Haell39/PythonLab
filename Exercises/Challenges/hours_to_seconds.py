# Função que recebe hora no formato horas minutos e segundos e retorna o total de segundos:

def time(): # do not need to pass h, m, s, and total_seconds as arguments because they are already defined in the function
    h = int(input('Enter the hours: '))
    m = int(input('Enter the minutes: '))
    s = int(input('Enter the seconds: '))
    total_seconds = h * 3600 + m * 60 + s
    print(f'The total seconds is {total_seconds}')


time()
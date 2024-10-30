# Implicit Type Casting (conversão implícita de tipos)
# Python automaticamente converte int para float quando necessário

x = 5       # int
y = 3.0     # float
z = x + y   # Resultado será float porque Python converte int para float automaticamente
print("Resultado de x + y com conversão implícita:", z)  # Saída: 8.0

# Explicit Type Casting (conversão explícita de tipos)
# Conversão manual de um tipo de dado para outro usando funções como int(), float() e str()

# Exemplo 1: Float para Int
a = 10.89
print("Conversão explícita de float para int:", int(a))  # Saída: 10 (a parte decimal é removida)

# Exemplo 2: String para Float
b = "15"
print("Conversão explícita de string para float:", float(b))  # Saída: 15.0

# Exemplo 3: Int para String
c = 10
print("Conversão explícita de int para string:", str(c))  # Saída: '10' (agora é uma string)
print("Multiplicação de c por 2:", c * 2)  # Saída: 20 (multiplicação como int)

# Exemplo 4: String para Int
# Útil quando precisamos transformar valores numéricos em strings para cálculos

d = "42"
print("Conversão explícita de string para int:", int(d) + 8)  # Saída: 50

# Exemplo 5: Tentativa de conversão que gera erro
# Tente converter uma string com letras para int

try:
    e = "hello"
    print(int(e))  # Isso gerará um erro porque "hello" não pode ser convertido em int
except ValueError:
    print("Erro: Não é possível converter 'hello' para int")

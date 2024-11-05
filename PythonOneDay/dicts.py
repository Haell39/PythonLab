# Estudo sobre Dicionários em Python

""" O que é um Dicionário?
Um dicionário é uma coleção de pares de dados relacionados,
onde cada par consiste em uma chave e um valor. As chaves devem ser únicas. """

# 1. Criação de Dicionários
print("1. Criação de Dicionários")
myDict = {'Peter': 38, 'John': 45, 'Jana': 29}
print(myDict)

# 2. Chaves Únicas
print("\n2. Chaves Únicas")
myDict = {'Peter': 38, 'John': 45, 'Jana': 29, 'Jana': 30}  # O valor de 'Jana' será 30
print(myDict)

# 3. Usando a Função dict()
print("\n3. Usando a Função dict()")
userNameandAge = dict(Peter=38, Alvin=45, Elvin=29)
print("Idade de Alvin:", userNameandAge['Alvin'])  # Saída: 45

# Manipulação de Dicionários
print("\nManipulação de Dicionários")

# Atualizando Valores
userNameandAge['Alvin'] = 27
print("Nova idade de Alvin:", userNameandAge['Alvin'])  # Saída: 27

# Adicionando Novos Itens
userNameandAge['Joe'] = 33
print("Dicionário atualizado:", userNameandAge)  
# Saída: {'Peter': 38, 'Alvin': 27, 'Elvin': 29, 'Joe': 33}

# Criando um Dicionário Vazio
print("\nCriando um Dicionário Vazio")
myDict = dict()
myDict['Peter'] = 38
myDict['John'] = 45
myDict['Jana'] = 29
print("Dicionário vazio preenchido:", myDict)  
# Saída: {'Peter': 38, 'John': 45, 'Jana': 29}

# Exemplos Adicionais
print("\nExemplos Adicionais")
myDict2 = {'One': 1.35, 2.5: 'Two point five', 3: '+', 7.9: 2}
print("Dicionário com diferentes tipos:", myDict2)

# Acessando Valores
print("Acessando valores:")
print("Valor associado à chave 'One':", myDict2['One'])   # Saída: 1.35
print("Valor associado à chave 7.9:", myDict2[7.9])       # Saída: 2

# Atualizando Valores em Dicionários Existentes
myDict2[2.5] = 'Two and a half'
print("Atualizando valor da chave 2.5:", myDict2[2.5])     # Saída: Two and a half

# Adicionando e Removendo Itens
myDict2['New Item'] = 'New Value'
print("Após adicionar 'New Item':", myDict2)          # Saída inclui 'New Item'

del myDict2['New Item']
print("Após remover 'New Item':", myDict2)             # Saída sem 'New Item'

# Conclusão
print("\nConclusão:")
print("Os dicionários são uma estrutura de dados poderosa em Python que permite armazenar pares de chave-valor de forma eficiente.")
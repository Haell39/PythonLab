"""  Creating a String: """

letter = "P"
print(letter)
print(len(letter))
greeting = "Hello, World!"
setence = "I hope this works fine!!"
print(setence)


""" Multiline string: """

multilineString = """Tripple quotes generates a multiline
comment that can break spaces like '\\n' """  # --> and \\ double backslash can be used to print \n, you can --> \\n, that way \n will appear

print(multilineString)


""" String Concatenation: """

firstName = "Rael"
lastName = "Santos"
space = " "

fullName = firstName + space + lastName
print(fullName)
print(firstName, lastName, sep=" ")

print(len(firstName) > len(lastName))
print(len(fullName))


""" Escape Sequences in Strings: """

# --> ^^ In Python and other programming languages \ followed by a character is an escape sequence
"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""

# --> exemples:

print(f"Topics: Days\tPlays\t Games")

print('This is a backslash symbol (\\)') # To write a special charecter use \
print("I am a pro player in \"Hello, World!\" other people and languages")


""" String Interpolation / f-Strings (Python 3.6+): """

a = 4
b = 7

print(f'{a} + {b} = {a + b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a**b}')

"""
OBS: Division in python -->

resultado = 10 / 3 -> realiza a divisão padrão entre dois números
print(resultado)  # Saída: 3.3333333333333335

resultado = 10 // 3 -> realiza a divisão inteira, retornando apenas a parte inteira do resultado da divisão, descartando qualquer fração
print(resultado)  # Saída: 3

resultado = 10 % 3 -> retorna o resto da divisão entre dois números
print(resultado)  # Saída: 1

| Operador | Descrição                             | Resultado Exemplo |
|----------|---------------------------------------|--------------------|
| `/`      | Divisão normal (float)               | `10 / 3 = 3.333...`|
| `//`     | Divisão inteira (parte inteira)       | `10 // 3 = 3`      |
| `%`      | Resto da divisão                      | `10 % 3 = 1`       |
"""



""" Accessing Characters in Strings by Index: """

lang = 'python'
firstLetter = lang[0]
print(firstLetter)
secondLetter = lang[1]
print(secondLetter)
lastIndex = len(lang) -1 # -1 return the last index in any given array
lastLetter = lang[lastIndex]
print(lastIndex)
print(lastLetter)

""" If we want to start from right end we can use negative indexing. -1 is the last index: """

language = 'Python'
last_Letter = language[-1]
print(last_Letter)
secondLast = language[-2]
print(secondLast)

""" Slicing Python Strings: 
In python we can slice strings into substrings --> """

langtest = 'PyMaster'
firstTWO = langtest[0:2] # The last num doesnt count -> exple: 0:7 only counts the follow indexes -> 0 1 2 3 4 5 6, NOT the last (7)
print(firstTWO)

lastTHREE = langtest[5:8] # --> 8, to include 5 6 and the last (7)
print(lastTHREE)
lastTHREEb = langtest[-3:] # Another way to print the 3 last letters, demanding the code to go for the last index and rollback n indexes(3 in case) asked, counting with the last
print(lastTHREEb) 
lastTHREEc = langtest[5:] # Another way to print the 3 last letters, is like we demand the code go from 5 --> to the last index
print(lastTHREEc)

""" Reversing a String: """

godPython = 'Hello, Python!'
print(godPython[::-1])
myName = 'Rafael Andrade Dutra dos Santos'
print(myName.lower()[::-1])
print(myName.upper()[::-1])

""" Skipping Characters While Slicing: """

langtest2 = 'Python'
pto = langtest2[0:6:2] # the last algarism is the index, the code goes from 0 to the last index (6), skipping 2 indexes counting fromw where it is -->
# ^^ P 1 2 (P counts) T 1 2 (t counts) O 
print(pto)

""" << String Methods: """



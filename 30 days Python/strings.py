# day 4
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

print("This is a backslash symbol (\\)")  # To write a special charecter use \
print('I am a pro player in "Hello, World!" other people and languages')


""" String Interpolation / f-Strings (Python 3.6+): """

a = 4
b = 7

print(f"{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a**b}")

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

lang = "python"
firstLetter = lang[0]
print(firstLetter)
secondLetter = lang[1]
print(secondLetter)
lastIndex = len(lang) - 1  # -1 return the last index in any given array
lastLetter = lang[lastIndex]
print(lastIndex)
print(lastLetter)

""" If we want to start from right end we can use negative indexing. -1 is the last index: """

language = "Python"
last_Letter = language[-1]
print(last_Letter)
secondLast = language[-2]
print(secondLast)

""" Slicing Python Strings: 
In python we can slice strings into substrings --> """

langtest = "PyMaster"
firstTWO = langtest[
    0:2
]  # The last num doesnt count -> exple: 0:7 only counts the follow indexes -> 0 1 2 3 4 5 6, NOT the last (7)
print(firstTWO)

lastTHREE = langtest[5:8]  # --> 8, to include 5 6 and the last (7)
print(lastTHREE)
lastTHREEb = langtest[
    -3:
]  # Another way to print the 3 last letters, demanding the code to go for the last index and rollback n indexes(3 in case) asked, counting with the last
print(lastTHREEb)
lastTHREEc = langtest[
    5:
]  # Another way to print the 3 last letters, is like we demand the code go from 5 --> to the last index
print(lastTHREEc)

""" Reversing a String: """

godPython = "Hello, Python!"
print(godPython[::-1])
myName = "Rafael Andrade Dutra dos Santos"
print(myName.lower()[::-1])
print(myName.upper()[::-1])

""" Skipping Characters While Slicing: """

langtest2 = "Python"
pto = langtest2[
    0:6:2
]  # the last algarism is the index, the code goes from 0 to the last index (6), skipping 2 indexes counting fromw where it is -->
# ^^ P 1 2 (P counts) T 1 2 (t counts) O
print(pto)

# << String Methods in Python

# Capitalization Methods
challenge = "thirty days of python"
print(challenge.capitalize())  # Output: "Thirty days of python"
print(challenge.title())  # Output: "Thirty Days Of Python"

# Count Method
counting = "thirty days of python"
print(counting.count("y"))  # Returns the occurrences of "y"
print(counting.count("y", 5, 14))  # Count "y" from index 5 to 14
print(counting.count("th"))  # Returns the occurrences of "th"

# Endswith Method
end_with = "thirty days of python"
print(end_with.endswith("on"))  # Output: True
print(end_with.endswith("tion"))  # Output: False

# Case Conversion
low = "Tird DAYS Of PyTHon"
print(low.lower())  # Output: "tird days of python"

up = "thirty days of python"
print(up.upper())  # Output: "THIRTY DAYS OF PYTHON"

# Strip Methods
striper = "    Hello    "
striperB = "$$$HelloA$$$$"

print(striper.strip())  # Removes surrounding whitespace
print(striperB.strip("$"))  # Removes surrounding "$"

LRSstriper = "###HELO###"
print(LRSstriper.lstrip("#"))  # Removes leading "#"
print(LRSstriper.rstrip("#"))  # Removes trailing "#"

# Split and Join Methods
splitter = "Hello World"
print(splitter.split())  # Splits by whitespace into ["Hello", "World"]

lista = "apple, banana, kaki"
print(lista.split(","))  # Splits by comma into ["apple", " banana", " kaki"]

words = ["Hello", "Python"]
print(" ".join(words))  # Joins list into "Hello Python"

# Replace Method
hello = "Hello, Python!"
print(hello.replace("Python", "World"))  # Output: "Hello, World!"

# Find Method
finder = "Hello World"
print(finder.find("world"))  # Output: -1 (not found)
print(finder.find("World"))  # Output: 6 (index of "World")

# Startswith and Endswith Methods
begin = "Hello, Worlds!!"
print(begin.startswith("hello"))  # Output: False
print(begin.startswith("Hello"))  # Output: True
print(begin.endswith("Worlds"))  # Output: False
print(begin.endswith("Worlds!!"))  # Output: True

# Check Methods
# isdigit
digit = "1234567890"
digit2 = "1234567890A"
print(digit.isdigit())  # Output: True
print(digit2.isdigit())  # Output: False

# isalpha
alphabetic = "HelOou"
alphabetic2 = "HelO3ou"
print(alphabetic.isalpha())  # Output: True
print(alphabetic2.isalpha())  # Output: False

# isalnum
alphanumeric = "123Alphabet"
alphanumeric2 = "123 Alphabet"  # Space is not alphanumeric
print(alphanumeric.isalnum())  # Output: True
print(alphanumeric2.isalnum())  # Output: False

# Partition Method
s = "hello world"
print(s.partition(" "))  # Splits into ("hello", " ", "world")

# Formatting Strings
name = "rael"
age = 25
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")  # New and better way

# Encode Method
a = "hello"
print(a.encode())  # Encodes string to bytes

# Casefold Method
s = "HELLOß"
print(s.casefold())  # Output: "helloss"

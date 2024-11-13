f = open ('PythonOneDay/bancoDados/myFile.txt')

firstLine = f.readline()
secondLine = f.readline()

print(firstLine, secondLine, sep='\n')

f.close()


"""
'r' mode:
For reading only.

'w' mode:
For writing only.
If the specified file does not exist, it will be created.
If the specified file exists, any existing data on the file will be erased.

'a' mode:
For appending.
If the specified file does not exist, it will be created.
If the specified file exist, any data written to the file is automatically added
to the end

'r+' mode:
For both reading and writing.

"""

f = open('PythonOneDay/bancoDados/myFile2.txt', 'w')

firstLine = f.write('This is a new line\n')
print(firstLine)
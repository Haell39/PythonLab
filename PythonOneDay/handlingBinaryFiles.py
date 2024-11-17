"""
Binary files store data in a format that is not meant to be human-readable, like images, videos, or audio files. Unlike text files (which store data as plain text), binary files store data in a format that the computer can interpret and process more efficiently.

In Python, you can read and write binary files using the rb (read binary) and wb (write binary) modes in the open() function.
"""


inputFile = open('PythonOneDay/IMGs/myimg.jpg', 'rb')

outputFile = open('PythonOneDay/IMGs/myoutputimg.jpg', 'wb')

#To read the binary data from the input file, you can use the read() method. This will return the content as a byte object.

data = inputFile.read()
outputFile.write(data)

inputFile.close()
outputFile.close()
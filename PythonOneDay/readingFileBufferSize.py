"""
Reading a file by buffer size using the read() function.
This approach helps save memory resources by reading a specified number of characters at a time.
"""

try:
    # Open the input file in read mode and output file in write mode
    with open('PythonOneDay/bancoDados/myFile4.txt', 'r') as inputFile, \
         open('PythonOneDay/bancoDados/myoutputfile.txt', 'w') as outputFile:

        buffer_size = 10  # Number of characters to read at a time
        msg = inputFile.read(buffer_size)

        while len(msg) > 0:
            outputFile.write(msg)
            msg = inputFile.read(buffer_size)

    print("Content successfully copied to 'myoutputfile.txt'")

except FileNotFoundError:
    print("Error: One of the files was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# =============================
# ^^ Example 1: Reading a File ('r' mode)
# =============================
try:
    f = open('PythonOneDay/bancoDados/myFile.txt', 'r')  # Opening file in read mode
    firstLine = f.readline()
    secondLine = f.readline()
    
    print("Reading from 'myFile.txt':")
    print(firstLine, secondLine, sep='\n')

except FileNotFoundError:
    print("Error: 'myFile.txt' not found.")
finally:
    f.close()  # Ensure file is closed
    print("\nFile closed after reading.\n")


# =============================
# ^^ Example 2: Writing to a File ('w' mode)
# =============================
try:
    f = open('PythonOneDay/bancoDados/myFile2.txt', 'w')  # Opening file in write mode
    # Write to file
    chars_written = f.write('This is a new line written with write mode\n')
    print(f"Number of characters written: {chars_written}")
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    f.close()
    print("File closed after writing.\n")


# =============================
# ^^ Example 3: Appending to a File ('a' mode)
# =============================
try:
    f = open('PythonOneDay/bancoDados/myFile2.txt', 'a')  # Opening file in append mode
    f.write("Appending a new line\n")
    print("New line appended to 'myFile2.txt'")
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    f.close()
    print("File closed after appending.\n")


# =============================
# ^^ Example 4: Reading and Writing ('r+' mode)
# =============================
try:
    f = open('PythonOneDay/bancoDados/myFile2.txt', 'r+')  # Opening file in read+write mode
    content = f.read()
    print("\nReading the content of 'myFile2.txt':")
    print(content)
    
    # Move cursor to the end and write additional content
    f.write("Added this line using 'r+' mode.\n")
    print("New line added using 'r+' mode")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    f.close()
    print("File closed after reading and writing.\n")




"""
=== ^^ Writing Files ===
Now that we’ve learned how to open and read a file, let’s try writing to it.
To do that, we’ll use the ‘a’ (append) mode. You can also use the ‘w’
mode, but you’ll erase all previous content in the file if the file already
exists.
"""



try:
    with open('PythonOneDay/bancoDados/myFile3.txt', 'a') as f:
        print('Writing to myFile3.txt')
        f.write('\nAppending a new line')
        f.write('\nAdding another line')
        f.close
except FileNotFoundError:
    print('File not Found!')
except Exception as e:
    print(f'Unexpected error: {e}')

# === Now reading File 3 ===

try:
    with open('PythonOneDay/bancoDados/myFile3.txt', 'r') as f:
        print('\nReading myFile3')
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print('File not Found!')
except Exception as e:
    print(f'Unexpected error: {e}')
    
    

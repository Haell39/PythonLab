# =============================
# Example 1: Reading All Lines and Looping through Lines
# =============================
try:
    print("\n--- Example 1: Reading 'myFile.txt' ---")
    with open('PythonOneDay/bancoDados/myFile.txt', 'r') as f:
        print("Reading all lines using 'with' statement:")
        for line in f:
            print(line.strip())  # strip() removes any extra newlines
except FileNotFoundError:
    print("Error: 'myFile.txt' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# =============================
# Example 2: Reading 'myFile3.txt'
# =============================
try:
    print("\n == Exemple 2 --> File 3")
    with open('PythonOneDay/bancoDados/myFile3.txt') as f:
        print("Trying to read file 3")
        for line in f:
            print(line, end='') # --> end='' remove \n
except FileNotFoundError:
    print("File not Found!!")
except Exception as e:
    print(f'Unexpected error: {e}')

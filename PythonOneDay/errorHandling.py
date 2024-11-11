
try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    answer = n1 / n2
    print(f'The answer is {answer:.2f}')

    with open("missing.txt", w) as file:
        content = file.read()
    
except ValueError:
    print("You did not enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except Exception as e:
    print(f"Unkown Error occurred: {e}")


# printing predefined py error {e} 

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The result of {a} / {b} is: {a / b}")
except ValueError as e: print(e)

try:
    # Intentionally cause a division by zero error
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result:.2f}")

# Catch any kind of error and display it
except Exception as e:
    print("Unknown error:", e)

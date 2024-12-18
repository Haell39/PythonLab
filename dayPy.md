### **Python Variables - A Complete Master Class (Day 2)** 🚀  

Welcome to Day 2! Variables are **foundational** in Python. Let’s break this into simple steps with practical **examples**, **concepts**, and mini **challenges** to master variables.

---

## **1. What is a Variable?** 🤔  

A **variable** is a "container" to store data.  
- In Python, you **don’t need to declare the type** of variable.  
- Python automatically detects the data type.

---

### **2. Creating Variables in Python** 🛠️  

To create a variable:  
```python
# Syntax: variable_name = value
Must start with a letter or an underscore (_).
Can contain letters, numbers, and underscores.
Cannot use spaces or special characters (like @, #, $).
Case-sensitive: age and Age are different.
"""
name = "Alice"       # String (text)
age = 25             # Integer (whole number)
height = 5.8         # Float (decimal)
is_student = True    # Boolean (True or False)

print(name)          # Output: Alice
print(age)           # Output: 25
```

✅ **Rules for Naming Variables**:  
1. Must start with a **letter** or an **underscore** (_).  
2. Can contain letters, numbers, and underscores.  
3. Cannot use spaces or special characters (like `@, #, $`).  
4. Case-sensitive: `age` and `Age` are different.  

```python
my_name = "John"  # ✅ valid
_age = 30         # ✅ valid
2days = "Sunday"  # ❌ invalid (cannot start with a number)
```

---

## **3. Data Types in Variables** 🧵  

Python has several **data types**:  

| **Data Type** | **Example**          |
|---------------|----------------------|
| String        | `"Hello World"`      |
| Integer       | `10, -5, 0`          |
| Float         | `3.14, -2.5, 0.0`    |
| Boolean       | `True, False`        |
| None          | `None` (empty value) |

You can check the data type of a variable with `type()`:  

```python
x = "Hello"
y = 10
z = 3.5

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'float'>
```

---

## **4. Changing Variable Values** 🔄  

Variables can be reassigned:  
```python
age = 20
print(age)    # Output: 20

age = 25      # Changing value
print(age)    # Output: 25
```

You can also assign **multiple variables** in one line:  
```python
a, b, c = 1, 2, 3
print(a, b, c)   # Output: 1 2 3
```

Or assign the **same value** to multiple variables:  
```python
x = y = z = 10
print(x, y, z)   # Output: 10 10 10
```

---

## **5. Variable Scope** 📍  

### **Global Scope** (Accessible everywhere):  
```python
x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10
print(x)       # Output: 10
```

### **Local Scope** (Accessible only inside a function):  
```python
def my_function():
    y = 20  # Local variable
    print(y)

my_function()  # Output: 20
# print(y)     # Error: y is not defined outside the function
```

---

## **6. Special Variables - Strings and Numbers** 📊  

### Strings  
You can manipulate text (strings):  
```python
name = "Python"

# String concatenation
greeting = "Hello " + name
print(greeting)      # Output: Hello Python

# Repeating strings
repeat = name * 3
print(repeat)        # Output: PythonPythonPython
```

### Numbers  
You can perform arithmetic operations with numbers:  
```python
a = 10
b = 3

# Arithmetic operations
print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000
```

---

## **7. Input and Variables (User Input)** 🧑‍💻  

Take input from the user using `input()` function:  
```python
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name + "!", "You are", age, "years old.")
```

✅ **Note**: Input is always a **string**. Convert to integer or float if needed:  
```python
num = int(input("Enter a number: "))  # Convert input to integer
print(num + 10)   # Adds 10 to the input number
```

---

## **8. Constant Variables** 🔒  

Constants are variables that should **not change**. By convention, write constants in **UPPERCASE**:  
```python
PI = 3.14
GRAVITY = 9.8
print(PI, GRAVITY)
```

---

## **9. Mini Challenges 🧩**  

1. **Simple Math Program**:  
   Write a program to take two numbers as input and display their sum, product, and difference.  

2. **String Repeater**:  
   Ask the user for their name and a number. Print their name repeated that many times.

3. **Swapping Variables**:  
   Swap the values of two variables:  
   ```python
   a = 5
   b = 10
   # Swap values here
   print(a, b)   # Output: 10 5
   ```

4. **Age Calculator**:  
   Ask the user for their birth year and calculate their age.  

---

## **10. Quick Recap Checklist ✅**  

- [ ] What is a variable?  
- [ ] Naming rules for variables.  
- [ ] Types of data (string, integer, float, etc.).  
- [ ] How to check the data type.  
- [ ] Changing and reassigning variables.  
- [ ] Global vs. Local scope.  
- [ ] Taking user input.  

---

## **Next Steps 🚀**  

Master the above concepts, complete the challenges, and move on to **Day 3: Data Types Deep Dive**!  

If you want me to explain any topic in more detail or solve the challenges, let me know! 💻🔥
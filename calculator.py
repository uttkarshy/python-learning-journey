def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b   
def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator=input("Enter an operator (+, -, *, /): ")
if operator == '+':
    result = add(first_number, second_number)
elif operator == '-':
    result = subtract(first_number, second_number)
elif operator == '*':
    result = multiply(first_number, second_number)
elif operator == '/':
    result = divide(first_number, second_number)
else:
    result = "Error! Invalid operator."

print("The result is:", result)

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x *y
def divide(x,y):
    return x/y
print("Select an operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = int(input("Enter operation (1,2,3,4): "))
if operation == 1:
    print(f"{num1} + {num2} = {num1+ num2}")
elif operation == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Can't divide by 0!")
else:
    print("Select the correct operation!")


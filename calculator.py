x = float(input("Enter first number:  "))
y = float(input("Enter second number: "))
sign = (input("Enter the sign (+,-,*,/): "))

if sign =="+":
     print(f"{x} + {y} = {x+y}")
elif sign =="-":
     print(f"{x} - {y} = {x-y}")
elif sign =="*":
     print(f"{x} * {y} = {x*y}")
elif sign =="/":
 if y!= 0:
    print(f"{x} / {y} = {x/y}")
 else:
    print("Can't print by 0!")
else:
 print("Incorrect operation!")

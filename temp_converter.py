temp = float(input("Enter the temperature which needs to be converted: "))
unit = input("Enter the unit (C/F): ")
if unit =="C":
    F = (9/5* temp) + 32
    print(f"Temperature in Fahrenheit is : {F:.2f} F")
elif unit =="F":
    C = (temp-32)* 5/9
    print(f"Temperature in Celsius is : {C:.2f} C")
else:
    print("Please enter the unit properly (C/F)!")

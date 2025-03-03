# This is a very simple shopping cart program
total_amount = 0
item = input("Enter the item name:  ")
price = float(input(f"Enter the prize of {item} in $: "))
number= int(input(f"Enter the quantity(s) of {item} purchased : "))
total_amount += number*price
ask = input("Do you have more items? (Yes/No)  ")
while ask =="Yes":
    item = input("Enter the item name: ")
    price = float(input(f"Enter the prize of {item} in $"))
    number = int(input(f"Enter the quantity(s) of {item} purchased "))
    total_amount += price*number
    print(f"Your total amount is {total_amount}$ ")
    ask = input("Do you have more items? (Yes/No)")
else:
    print(f"Your total amount is {total_amount}$ ")
    print("Thank you for shopping at Target! Have a great day ahead!")
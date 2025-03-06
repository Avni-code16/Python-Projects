def palindrome_checker(string1):
    string1 = string1.lower()
    string1 = ''.join(char for char in string1 if char.isalnum())
    string2 = string1[::-1]
    if string2 == string1:
        print(f"{string1} is palindrome")
    else:
         print(f"{string1} is not palindrome")

def palindrome_number(num1):
    num1_str = str(num1)
    num2_str = num1_str[::-1] # the slicing syntax [start:stop:step]
    # takes the string from start to end with a step of -1, which means it processes the string backward.
    if num1_str == num2_str:
        print(f"{num1} is palindrome")
    else:
        print(f"{num1} is not palindrome")

print("Welcome to Palindrome Checker! ")
string_input = input("Please enter the string to check for Palindrome:  ")
palindrome_checker(string_input)
number_input = int(input("Please enter the number to check for Palindrome: "))
palindrome_number(number_input)

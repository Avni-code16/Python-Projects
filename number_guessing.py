import random
def number_guessing(num):
   target_number = random.randint(1,50)
   if num == target_number:
       print(f"Congratulations! The number {num} you guessed was correct! :)")
   else:
       print(f"Sorry, the correct number was {target_number}. Your guess was {num}.")

print("Welcome to number_guessing game!")
num_input = int(input("Please enter a number from 1 to 50:  "))
if 1 <= num_input <= 50:
  number_guessing(num_input)
else:
     print(f"Your number {num_input} is out of range! Please enter the number in range.")
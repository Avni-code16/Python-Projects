import random
def rules(): # Function
    print("Rules for the game: ")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")

def play_game(name):
    while True:
        game_human = input("Choose an option from Rock, Paper & Scissors:  ").lower()  # Convert input to lowercase
        if game_human in ["rock", "paper", "scissors"]:  # Use lowercase strings in the list
            break  # Exit the loop if the input is valid
        else:
            print("Invalid choice! Please choose an option from Rock, Paper & Scissors.")

    choices = ["rock", "paper", "scissors"]  # Use lowercase strings
    game_comp = random.choice(choices)  # No need for .lower() since choices are already lowercase
    print(f"{name} : {game_human}")
    print(f"Computer : {game_comp}")
    return game_human, game_comp  # Return the choices

def game(name,game_human,game_comp):
    if game_human == game_comp: # used local variable!! wrong
        print("Both choices are same! Its a tie!")
    elif game_human == "rock" and game_comp =="scissors":
        print(f"{name} has won! Rock crushes scissors!")
    elif game_human == "paper" and game_comp == "rock":
        print(f"{name} has won! Paper covers Rock!")
    elif game_human == "scissors" and game_comp == "paper":
        print(f"{name} has won! Scissors cuts Paper!")
    else:
        print(f"{name} has lost!")


print("Welcome to the rock_paper scissors game!")
name = input("Please enter your name :)   ")
while True:
    s = input("Please enter r for rules, p to play or q to quit:  ")
    if s =="q":
         break
    elif s == "p":
        human_choice, comp_choice = play_game(name)
        game(name,human_choice, comp_choice)
    elif  s == "r":
        rules()

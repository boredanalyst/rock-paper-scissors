## Rock Paper Scissors game

#3 Importing the necessary libraries and modules.
import random

## Setting up the main menu
main_menu = {
    1:"Start Game",
    2:"Instructions",
    3:"Exit",
}

def show_main_menu():
    print("---------------------------------------")
    print("MAIN MENU")
    for x in main_menu:
        print(f'{x} : {main_menu[x]}')
    user_choice = "" ## resets the user_choice variable.
    user_choice = input("Enter your choice's number: ")
    if user_choice == 1:
        start_game()
    elif user_choice == 2:
        get_help()
    elif user_choice == 3:
        exit()
    else: 
        print("Please provide a valid number.")
        show_main_menu()

def start_game():
    print("---------------------------------------")
    print("Game is starting")
    user_choice = "" ## resets the user_choice variable
    user_choice = input("Please enter your choice's number: ")
    if user_choice == "":
        print("Please input a valid choice:")
    

def get_help():
    print("---------------------------------------")
    print("INSTRUCTIONS")
    print("Hello there!")
    print("You will be playing a game of Rock, Paper, Scissors.")
    print("Yes, that game.")
    print("Every round, you will be asked to play a game of Rock, Paper, Scissors")
    print("You will be asked to provide the hand you want to play.")
    print("Once you have made that choice, the game will pit your hand against the opponent's")
    print("If you win, you'll get one point.")
    print("If you lose, the opponent will get a point.")
    print("The first player to win 3 points wins!")
   
    def repeat_info():
        user_choice = "" ## resets the user choice variable
        user_choice = input("Do you want to hear that explanation again?: ")
        if user_choice == "yes":
            get_help()
        elif user_choice == "no":
            show_main_menu()
        else: 
            print("Please provide a valid answer.")
            repeat_info()

def exit():
    print("---------------------------------------")
    print("The game will be ending soon.")


## Initializing the game.

options = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}

def start_game():
    print("---------------------------------------")
    print("STARTING GAME")
    user_point = 0
    enemy_point = 0
    play_round()
    
def play_round():
    user_pick_option()
    enemy_pick_option()
    showdown()
    check_user_point()
    check_enemy_point()   

def user_pick_option():
    for x in options:
        print(f'{x}: {options[x]}')
    user_choice = ""
    user_choice = input("Please choose your hand: ")
    if user_choice not in options:
        print("Please provide a valid answer.")
        user_pick_option()
    user_hand = options.get(user_choice)

def enemy_pick_option():
    enemy_hand = random.random()
    enemy_hand = options.get(enemy_hand)

def showdown():
    print(f'Player uses {user_hand}!')
    print(f'Enemy uses {enemy_hand}!')

    if user_hand == enemy_hand:
        print("It's a tie!")
    if user_hand == "Rock" and enemy_hand == "Paper":
        print("Enemy won!")
        enemy_point += 1
    if user_hand == "Rock" and enemy_hand == "Scissors":
        print("Player won!")
        user_point += 1
    if user_hand == "Paper" and enemy_hand == "Rock":
        print("Player won!")
        user_point += 1
    if user_hand == "Paper" and enemy_hand == "Scissors":
        print("Enemy won!")
        enemy_point += 1
    if user_hand == "Scissors" and enemy_hand == "Rock":
        print("Enemy won!")
        enemy_point += 1
    if user_hand == "Scissors" and enemy_hand == "Paper":
        print("Player won!")
        enemy_point += 1
    

def check_user_point():
    if user_point >= 5:
        user_win()
    else:
        check_enemy_point()

def check_enemy_point():
    if enemy_point >= 5:
        enemy_win()
    else:
        play_round()

def user_win():
    print("---------------------------------------")
    print("CONCLUSION")
    print("You won!")
    user_choice = ""
    user_choice = input("Do you want to play again?: ")
    if user_choice == "yes":
        start_game()
    elif user_choice == "no":
        show_main_menu()

def enemy_win():
    print("---------------------------------------")
    print("CONCLUSION")
    print("You lost...")
    user_choice = ""
    user_choice = input("Do you want to play again?: ")
    if user_choice == "yes":
        start_round()
    elif user_choice == "no":
        show_main_menu()


## Flow of the game

show_main_menu()
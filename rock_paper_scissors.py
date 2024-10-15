# Required Libraries
import random, time
import sys

# Lists
pcomp = []
puser = []

# Functions
def pointComputer():
    pcomp.append("*")
    if(len(pcomp) == 5):
        print("Computer Won")
        print("Score: " , len(pcomp) , "-" , len(puser))
        questions()
        quit()

def pointUsers():
    puser.append("*")
    if (len(puser) == 5):
        print("User Won")
        print("Score: ", len(pcomp), "-", len(puser))
        questions()
        quit()

def soc():
    return random.choice(r_p_s).lower()

def start_again():
    print("the game starts again")
    start_game()

def exit():
    print("The Game Gets Closed")
    time.sleep(1)
    print("Thank you for playing the game...Good Bye")
    time.sleep(1.5)
    sys.exit()

def welcome():
    print("Welcome to Rock Paper Scissors Game")
    time.sleep(1)
    print("enjoy")
    time.sleep(1)
    print("Rock = 'R' or 'r'")
    time.sleep(0.5)
    print("Paper = 'P' or 'p'")
    time.sleep(0.5)
    print("Scissors = 'S' or 's'")
    time.sleep(0.5)

def border():
    print("/"*50)

def questions():
    a = input("Do you want to play again?(Y/N): ").lower()  # Küçük harfe çevir
    if a == 'y':
        start_again()
    elif a == 'n':
        exit()
    else:
        print("Invalid Selection")
        questions()

# Game Options (Rock, Paper, Scissors)
r_p_s = ['r','p','s']

# Game Logic
def start_game():
    welcome()
    border()
    print("The one who reaches a score of 5 wins.")
    while True:
        Selection_of_computer = soc()

        user = input("You Have to Choose Between Rock, Paper, Scissors: ").lower()  # Kullanıcı seçimi küçük harfe çevriliyor

        if Selection_of_computer == 'r' and user == 's':
            print("You lost! Rock is stronger than Scissors.")
            border()
            pointComputer()

        elif Selection_of_computer == 'p' and user == 'r':
            print("You lost! Paper is stronger than Rock.")
            border()
            pointComputer()

        elif Selection_of_computer == 's' and user == 'p':
            print("You lost! Scissors is stronger than Paper.")
            border()
            pointComputer()

        elif Selection_of_computer == 's' and user == 'r':
            print("You won! Rock is stronger than Scissors.")
            border()
            pointUsers()

        elif Selection_of_computer == 'r' and user == 'p':
            print("You won! Paper is stronger than Rock.")
            border()
            pointUsers()

        elif Selection_of_computer == 'p' and user == 's':
            print("You won! Scissors is stronger than Paper.")
            border()
            pointUsers()

        elif Selection_of_computer == user:  # Beraberlik durumu
            print("It's a tie!")
            border()

        else:
            print("Invalid Value")
            border()

start_game()
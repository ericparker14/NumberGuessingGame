from os import system, name
from random import randint
from art import logo
# Turns for the player
EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5


def difficulty():
    """Sets the difficulty of the game by user choice"""
    level = input("Choose a difficulty: 'easy' or 'hard'")
    if level == "easy":
        return EASY_MODE_TURNS
    else:
        return HARD_MODE_TURNS


def clear():
    """Used to clear the terminal screen"""
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('clear')


def compare_guess(user_num, answer, lives):
    """Function to compare the user guess to the actual, and remove lives if wrong."""
    if user_num > answer:
        print(f"Your guess of {user_num} is too high")
        return lives - 1
    elif user_num < answer:
        print(f"Your guess of {user_num} is too low")
        return lives - 1
    else:
        print("You win! Your guess is correct!")


def game():
    """To run the game functionality if the user says yes to play game"""
    clear()
    print(logo)
    answer = randint(1, 100)
    # some opening statements
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100...")
    print(f"P.S. the answer is {answer}")
    is_game_over = False
    turns = difficulty()
    guess = 0
    while guess != answer:
        guess = int(input("What is your guess?\n"))
        turns = compare_guess(user_num=guess, answer=answer, lives=turns)
        if turns == 0:
            print(f"You have {turns} lives left, you lose. The answer was {answer}")
            return is_game_over
        elif guess != answer:
            print(f"You have {turns} left, guess again!")


while input("Do you want to play the number picker game? Enter 'y' for yes and 'n' for no\n") == "y":
    game()


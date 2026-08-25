import random
from q2 import *

def get_guesses():
    """Get guesses from user."""
    my_guess = []
    for i in range(3):
        number = int(input(f"Enter guess {i+1}: "))
        my_guess.append(number)
    return my_guess


def generate_solution():
    """Create a solution from random generator."""
    solution = []
    for i in range(3):
        solution.append(random.randint(1, 3))
    return solution


def main():
    """Start of game."""
    # 1. generate a list of random numbers of SIZE 3
    game_solution = generate_solution()

    # 2. ask the user to guess 3 numbers
    my_guess = get_guesses()

    # 3. retrieve the number of points from guess()
    points = guess(game_solution, my_guess)
    print("Number of points: ", points)
    while points != 3:
        print("Not all correct guesses were made. Please try again.")
        my_guess = get_guesses()
        points = guess(game_solution, my_guess)
        print("Number of points: ", points)


if __name__ == '__main__':
    main()
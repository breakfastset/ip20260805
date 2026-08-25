def guess(solution, my_guess):
    """
    Return the number of correct guesses.
    Each correct number in the correct position
    is considered a correct guess.
    """
    total = 0
    for i in range (len(solution)):
        if solution[i] == my_guess[i]:
            total += 1
    return total


def main():
    """Start of program."""
    print("--- Test 1: Correct solution ---")
    print(guess([1, 2, 3, 4], [1, 2, 3, 4]))
    print("--- Test 2: 2 Correct guesses ---")
    print(guess([1, 2, 2, 1], [1, 2, 1, 2]))

if __name__ == '__main__':   # if you are executing this file
    main()   # run main
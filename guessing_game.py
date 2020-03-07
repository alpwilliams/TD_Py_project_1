import random




def start_game():
    # 1) Display an intro/welcome message to the player
    print("Welcome to the Guessing Game!")

    high_score = 0
    guess_count = 0
    play = 'Y'

    # 2) Store a random number as the answer/solution
    answer = random.randint(0,10)

    # 3) Continuously prompt the player for a guess.
    
    while play == 'Y':
        guess = input("Please guess a number between 1 and 10: ")
        guess = int(guess)

        # 3a) If the guess greater than the solution, display to the player "It's lower"
        if guess > answer:
            print("It's lower.")
            # increment number of guesses by 1
            guess_count = int(guess_count + 1)
            continue

        # 3b) If the guess is less than the solution, display to the player "It's higher"
        elif guess < answer:
            print("It's higher")
            # increment number of guesses by 1
            guess_count = int(guess_count + 1)
            continue

        # 4) Once the guess is correct, stop looping, inform the user they "Got it"
        elif guess == answer:
            print("Got it!")
            # High Score Check
            if guess_count < high_score:
                high_score = guess_count
            # 4a) Show how many attempts it took them to get the correct number
            print("You took {} attempts to get the correct number.".format(guess_count))

    """Psuedo-code Hints
    

    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

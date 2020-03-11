import random
import time

def start_game():
    # 1) Display an intro/welcome message to the player
    print("""
    -----------------------------------
    | Welcome to the GUESSING GAME!!! |
    -----------------------------------
    """)

    # Declare Default Variable Values
    high_score = 0
    guess_count = 1
    success = 0
    error = 0
    play = 'y'

    # 2) Store a random number as the answer/solution
    answer = random.randint(1,10)

    # 3) Continuously prompt the player for a guess.
    while play.lower() == 'y':
        time.sleep(.5)
        guess = input("Please guess a number between 1 and 10: ")
        print("Checking your guess")
        time.sleep(.25)
        print(".")
        time.sleep(.25)
        print(".")
        time.sleep(.25)
        # Error counter (Easter Egg)
        if error > 5 and error < 7:
            time.sleep(.5)
            print("Y tho?")
            error = 7
            time.sleep(.5)
        elif error > 8 and error < 10:
            time.sleep(.5)
            print("Seriously...")
            error = 9
            time.sleep(.5)
        elif error > 10:
            time.sleep(.5)
            print("Aight I'm out, system shutting down ☉_☉")
            break
        try:
            guess = int(guess)
        except ValueError:
            print("Oh no! (╥﹏╥)")
            time.sleep(1.5)
            print("That's not a valid selection")
            time.sleep(1)
            print("Try only entering a number between 1 and 10 as your guess")
            time.sleep(1)
            print("Please try again")
            time.sleep(2)
        else:
            if guess < 1:
                time.sleep(.5)
                print("That guess below 1!")
                error = error + 1
            elif guess > 10:
                time.sleep(.5)
                print("That guess is above 10!")
                error = error + 1

            # 3a) If the guess greater than the solution, display to the player "It's lower"
            elif guess > answer:
                print(".")
                time.sleep(.5)
                print("It's lower")
                time.sleep(.25)
                # increment number of guesses by 1
                guess_count = guess_count + 1
                # reset error counter
                error = 0
                continue

            # 3b) If the guess is less than the solution, display to the player "It's higher"
            elif guess < answer:
                print(".")
                time.sleep(.5)
                print("It's higher")
                time.sleep(.25)
                # increment number of guesses by 1
                guess_count = guess_count + 1
                # reset error counter
                error = 0
                continue

            # 4) Once the guess is correct, stop looping, inform the user they "Got it"
            elif guess == answer:
                time.sleep(.25)
                print("!")
                time.sleep(.5)
                print("(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧ YOU GOT IT!!!")
                time.sleep(1.5)
                print("Congratulations!!!")
                time.sleep(1.5)
                #increment successful games by 1
                success = success + 1
                # High Score Check
                if success == 1:
                    high_score = guess_count
                elif guess_count < high_score:
                    high_score = guess_count

                # 4a) Show how many attempts it took them to get the correct number
                print("You took {} attempts to get the correct number".format(guess_count))
                time.sleep(1)
                # Display High Score
                print("Your current best is {} attempt(s) before guessing the correct number".format(high_score))
                time.sleep(1)
                # Reset guess count
                guess_count = 1
                # Ask User if they would like to play again
                play = input("Would you like to play again? Please type Y to try again and N to exit the game:  ")
                if play.lower() != 'y':
                    # 5) Let the player know the game is ending, or something that indicates the game is over
                    print("Thanks for playing, your best game was {} attempt(s)! See you next time!".format(high_score))
                    time.sleep(2.5)

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
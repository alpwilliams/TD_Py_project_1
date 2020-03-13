import random
import time

def start_game():
    # Display an intro/welcome message to the player
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

    # (Initial) Store a random number as the answer/solution
    answer = random.randint(1,10)

    # Continuously prompt the player for a guess.
    while play.lower() == 'y':
        time.sleep(.5)
        if guess_count == 1 and error == 0:
            if high_score >= 3:
                print("""
The score to beat is {} attempt(s)! Do it in {} tries or fewer to be the new Guessing Game Champ!""".format(high_score, high_score - 1))
                time.sleep(1.5)
            elif high_score == 2:
                print("""
The score to beat is {} attempt(s)! Do it in {} try to show off your DIGITAL TELEPATHY!!!""".format(high_score, high_score -1 ))
                time.sleep(1.5)
            elif high_score == 1:
                print("""
Great job at setting the high score to {} attempt! Try to do it again!""".format(high_score))
                time.sleep(1.5)
            elif high_score == 0:
                print("""
The high score is currently {}, which is impossible to achieve, so get as close as you can to 1!""".format(high_score))
                time.sleep(1.5)
        guess = input("""
Please guess a number between 1 and 10: """)
        print("Checking your guess")
        time.sleep(.25)
        print(".")
        time.sleep(.25)
        print(".")
        time.sleep(.25)
        
        # Error counter Easter Egg
        if error > 5 and error < 7:
            time.sleep(.5)
            print("8-|")
            time.sleep(.5)
            print("Y tho?")
            error = 7
            time.sleep(.5)
        elif error > 8 and error < 10:
            time.sleep(.5)
            print("9_9")
            time.sleep(.5)
            print("Seriously...")
            error = 9
            time.sleep(.5)
        elif error > 10:
            time.sleep(.5)
            print("☉_☉")
            time.sleep(.5)
            print("Aight I'm out, system shutting down...")
            time.sleep(.5)
            print("...")
            time.sleep(.5)
            print("..")
            time.sleep(.5)
            print(".")
            time.sleep(.5)
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
                print("X")
                time.sleep(.5)
                print("That guess is below 1!")
                time.sleep(.5)
                error = error + 1
            elif guess > 10 and guess < 9000:
                print("X")
                time.sleep(.5)
                print("That guess is above 10!")
                time.sleep(.5)
                error = error + 1
            # Over 9K easter egg per request :)
            elif guess > 9000:
                print("Vegeta! What did you say the guess was!?")
                time.sleep(1)
                print("It's over 9000!")
                time.sleep(1)
                print("For real though, that guess is way above 10")
                time.sleep(1)
                print("You are gonna stress Vegeta out, please chill lol")
                time.sleep(1)
                error = error + 1

            # If the guess greater than the solution, display to the player "It's lower"
            elif guess > answer:
                print(".")
                time.sleep(.5)
                print("It's lower")
                time.sleep(.25)
                # Increment number of guesses by 1
                guess_count = guess_count + 1
                # Reset error counter
                error = 0
                continue

            # If the guess is less than the solution, display to the player "It's higher"
            elif guess < answer:
                print(".")
                time.sleep(.5)
                print("It's higher")
                time.sleep(.25)
                # Increment number of guesses by 1
                guess_count = guess_count + 1
                # Reset error counter
                error = 0
                continue

            # Once the guess is correct, stop looping, inform the user they "Got it"
            elif guess == answer:
                time.sleep(.25)
                print("!")
                time.sleep(.5)
                print("(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧ YOU GOT IT!!!")
                time.sleep(1.5)
                print("Congratulations!!!")
                time.sleep(1.5)
                # Increment successful games by 1
                success = success + 1
                # High Score Check
                if success == 1:
                    high_score = guess_count
                elif guess_count < high_score:
                    high_score = guess_count

                # Show how many attempts it took them to get the correct number
                print("You took {} attempts to get the correct number".format(guess_count))
                time.sleep(1)
                # Display High Score
                print("Your current best is {} attempt(s)".format(high_score))
                time.sleep(1)
                # Reset guess count for possible new game
                guess_count = 1
                # Refresh answer for possible new game
                answer = random.randint(1,10)
                # Ask User if they would like to play again
                play = input("Would you like to play again? Please type Y to try again and N to exit the game:  ")
                if play.lower() != 'y':
                    # Let the player know the game is ending, or something that indicates the game is over
                    print("Thanks for playing, your best game was {} attempt(s)! See you next time!".format(high_score))
                    time.sleep(1.5)
                    print("...")
                    time.sleep(.5)
                    print("..")
                    time.sleep(.5)
                    print(".")
                    time.sleep(.5)

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
import random

number = random.randint(1, 10)

player_name = input("Hello, human. What is your name?")
number_of_guesses = 0
print("Okay, " + player_name + ", I am guessing a number between 1 and 10. Can your weak human brain guess my number?"
                               " What is your guess?")

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number and number_of_guesses < 3:
        print("WRONG! Your guess is too low! Guess again.")
    if guess > number and number_of_guesses < 3:
        print("WRONG! Your guess is too high Guess again")
    if guess == number:
        break
if guess == number:
    print("AHHHHHH! You guessed my number in " + str(number_of_guesses) + " tries!")
else:
    print("HA! Stupid human! You did not guess my number. The number was " + str(number) + ". Your weak human brain"
                                                                                           " is no match for me!")

"""An example of conditional (if-else) statments"""

SECRET: int = 3

print("I'm thinking for a number 1-5, what is it?")
guess: int = int(input("Why is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else: 
        print("You guessed too low!")
print("Game over.")
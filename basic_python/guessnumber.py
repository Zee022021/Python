# Here we will give a title to our guessin game
game = "Welcome to 'Guess My Number'"
new_game = game.center(60)
print(new_game)

import random
the_number = random.randint(1,100)

guess = 0

while guess != the_number:
    guess = int(input("Please guess the number: ")) 

    if guess > the_number:
        print("Player Guess Lower. . . \n")
    elif guess < the_number:
        print("Player Guess Higher. . . \n")
    else:
        print(f"Game Over! The number was {the_number}. The Player Wins!\n")
        break

    guess = random.randint(1,100)
    if guess > the_number:
        print("Computer Guess Lower. . . \n")
    elif guess < the_number:
        print("Computer Guess Higher. . . \n")
    else:
        print(f"Game Over! The number was {the_number}. The Computer Wins!\n")
        break


next = input("Press Enter to continue....")
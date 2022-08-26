import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.choice(range(0, 101))

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        guess_amount = 10

    elif difficulty == "hard":
        guess_amount = 5

    is_game_over = False
    while not is_game_over:

        guess = int(input("Take a guess: "))

        def compare(guess, number):
            if guess < number:
                print("Too low. Guess again!")

            elif guess > number:
                print("Too high. Guess again!")

            elif guess == number:
                print(f"You got it! The answer was {number}.")
                is_game_over = True

        compare(guess, number)

        if guess_amount > 1:
            guess_amount -= 1
            print(f"You have {guess_amount} attempts to guess the number left.")

        else:
            print("Game Over, You've run out of guesses!")
            is_game_over = True


play_game()

play_again = input("Do you want to play again? Type 'y' or 'n': ")

while play_again == "y":
    play_game()

else:
    print("Goodbye!")


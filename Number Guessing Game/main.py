"""
When the user executes the program, the program prompts the user to
guess a number between 1 and 100 in the terminal.
The user types in a number and the program gives feedback on whether
that number is too low or too high from the hidden number so the user
can adjust the next number.
he user can submit up to 10 numbers until they win or fail.
"""

from random import randint


def guess_a_number():
    """Game function."""

    number = randint(1, 100)
    attempt = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!\n"
          "I have selected a number between 1 and 100.\n"
          f"You have {max_attempts} attempts to guess the correct number.")

    while attempt < max_attempts:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
            if 1 <= guess <= 100:
                attempt += 1
                if guess > number:
                    if attempt < max_attempts:
                        print("Too high! Try again.")
                    else:
                        print(
                            f"Sorry! You ran out of attempts. The number was {number}.")
                elif guess < number:
                    if attempt < max_attempts:
                        print("Too low! Try again.")
                    else:
                        print(
                            f"Sorry! You ran out of attempts. The number was {number}.")
                else:
                    print(
                        f"Congratulations! You've guessed the correct number in {attempt} attempts.")
                    return
            else:
                print("Value you entered is not between 1 and 100.")
        except ValueError:
            print("Value entered is not a valid integer number.")


if __name__ == "__main__":
    guess_a_number()

"""Number guessing game"""

__author__ = "730767370"


def guess_a_number() -> None:
    """Determine secret number and check user guesses"""
    secret: int = 7
    guess = int(input("Guess a number:"))
    print("Your guess was", guess)

    # check if guess is correct
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    elif guess > secret:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()

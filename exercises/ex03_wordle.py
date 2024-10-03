"""Recreating Wordle game"""

__author__ = "730767370"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    GREEN_BOX: str = "\U0001F7E9"
    correct: str = GREEN_BOX * len(secret)
    won: bool = False
    # Check users guesses until game is won or no more guesses left
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        result = emojified(
            secret=secret, guess=input_guess(len_secret_word=len(secret))
        )
        print(result)
        if result == correct:
            print(f"You won in {turn}/6 turns!")
            won = True
        turn += 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(len_secret_word: int) -> str:
    "Prompt for guess and validate input"
    guess = input(f"Enter a {len_secret_word} character word: ")
    while len(guess) != len_secret_word:
        guess = input(f"That wasn't {len_secret_word} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if character is in a string"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(secret: str, guess: str) -> str:
    """Visually represent accuracy of guess with emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index: int = 0
    result: str = ""
    # determine which color box to use
    while index < len(guess):
        if secret[index] == guess[index]:
            result = result + GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        index += 1
    return result


if __name__ == "__main__":
    main(secret="codes")

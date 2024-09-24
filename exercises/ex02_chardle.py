"""Step towards Wordle"""

__author__ = "730767370"


def main() -> None:
    """Run program"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Collect input word and check if its valid"""
    input_word = input("Enter a 5-character word: ")
    # exit if input is not 5 characters
    if len(input_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return input_word


def input_letter() -> str:
    """Collect input character and check validity"""
    input_letter = input("Enter a single character: ")
    # exit if input is not 1 character
    if len(input_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return input_letter


def contains_char(word: str, letter: str) -> None:
    """Check how many instances of input character are in input word"""
    print("Searching for", letter, "in", word)
    count: int = 0
    # check each letter of string to see if it matches input character
    if word[0] == letter:
        print(letter, "found at index 0")
        count += 1
    if word[1] == letter:
        print(letter, "found at index 1")
        count += 1
    if word[2] == letter:
        print(letter, "found at index 2")
        count += 1
    if word[3] == letter:
        print(letter, "found at index 3")
        count += 1
    if word[4] == letter:
        print(letter, "found at index 4")
        count += 1
    if count == 0:
        print("No instances of", letter, "found in", word)
    elif count == 1:
        print(count, "instance of", letter, "found in", word)
    else:
        print(count, "instances of", letter, "found in", word)


if __name__ == "__main__":
    main()

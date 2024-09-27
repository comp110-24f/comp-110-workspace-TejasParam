"""Concetenate 2 input strings"""

__author__ = "730767370"


def main() -> None:
    """Run Program"""
    print(concat(string1=word1, string2=word2))


def concat(string1: str, string2: str) -> str:
    """Concatenate the 2 input strings"""
    return string1 + string2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    main()

"""Functions of dictionaries"""

__author__ = "730767370"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Switch keys and values of a dictionary"""
    new_dict: dict[str, str] = {}
    for key in input:
        for k in new_dict:
            # check if key exists
            if k == input[key]:
                raise KeyError("Error: Dupicate keys")
        new_dict[input[key]] = key
    return new_dict


def favorite_color(input: dict[str, str]) -> str:
    """Determine most popular favorite colors in a list of names and favorite colors"""

    # determine count of each color
    color_count: dict[str, int] = {}
    for key in input:
        if input[key] in color_count:
            color_count[input[key]] += 1
        else:
            color_count[input[key]] = 1

    # determine the max amount a color had
    max = 0
    for key in color_count:
        if color_count[key] > max:
            max = color_count[key]

    # determine which color had the max amount
    max_keys = []
    for key in color_count:
        if color_count[key] == max:
            max_keys.append(key)

    # return the first instance
    if len(max_keys) > 0:
        return max_keys[0]
    else:
        return ""


def count(input: list[str]) -> dict[str, int]:
    """Count of each value in input dictionary"""
    count: dict[str, int] = {}
    # update key or add it if it doesnt exist
    for i in input:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """return dict with list of words starting with each letter"""
    letters: dict[str, list[str]] = {}
    # update key or add it if it doesnt exist
    for i in input:
        if i.lower()[0] in letters:
            letters[i.lower()[0]].append(i)
        else:
            letters[i.lower()[0]] = []
            letters[i.lower()[0]].append(i)
    return letters


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    """Update attendance based on name and day"""
    # update key or add it if it doesnt exist
    if day in attendance:
        if name not in attendance[day]:
            attendance[day].append(name)
    else:
        attendance[day] = []
        attendance[day].append(name)

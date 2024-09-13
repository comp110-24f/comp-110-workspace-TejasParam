"""Determine quantity of teabags, treats and cost for a tea party"""

__author__ = "730767370"


# print all info
def main_planner(guests: int) -> None:
    """Entrypoint of the program"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


# 2 tea bags per person
def tea_bags(people: int) -> int:
    """Determine how many teabags are needed base on number of guests"""
    return people * 2


# 1.5 treats per teabag
def treats(people: int) -> int:
    """Determine how many treats are needed base on number of guests"""
    return int(tea_bags(people=people) * 1.5)


# 50 cents per teabage and 75 cents per treat
def cost(tea_count: int, treat_count: int) -> float:
    """Determine cost of tea party"""
    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

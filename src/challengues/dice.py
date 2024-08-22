from random import randint
from collections import Counter


def roll_dice(*dices, trials=1000000):
    counts = Counter()
    for _ in range(trials):
        outcome = sum((randint(1, sides) for sides in dices))
        counts[outcome] += 1

    print("\nOUTCOME\tPROBABILITY")
    for outcome in range(len(dices), sum(dices) + 1):
        print(f"{outcome}\t{counts[outcome] * 100 / trials :0.2f}%")


if __name__ == "__main__":
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)

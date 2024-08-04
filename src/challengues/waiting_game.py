import time
import random


def waiting_game():
    target = random.randint(2, 4)
    print(f"Your target time is {target} seconds")

    input("Press Enter to begin")
    start = time.perf_counter()

    input("Press Enter again to finish")
    elapsed = time.perf_counter() - start

    if elapsed == target:
        print("Unbelievable! Perfect timing!")
    elif elapsed < target:
        print(f"{target - elapsed} seconds too fast")
    else:
        print(f"{elapsed - target} seconds too slow")


waiting_game()

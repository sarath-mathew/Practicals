import random

RANDOM_NUM_ONE = 0
RANDOM_NUM_TWO = 0
RANDOM_NUM_THREE = 0
RANDOM_NUM_FOUR = 0
RANDOM_NUM_FIVE = 0
RANDOM_NUM_SIX = 0


def main():
    quick_picks = int(input("How many quick picks?"))
    for i in range(quick_picks):
        RANDOM_NUM_ONE = random.randint(1, 45)
        RANDOM_NUM_TWO = random.randint(1, 45)
        RANDOM_NUM_THREE = random.randint(1, 45)
        RANDOM_NUM_FOUR = random.randint(1, 45)
        RANDOM_NUM_FIVE = random.randint(1, 45)
        RANDOM_NUM_SIX = random.randint(1, 45)

        quick_pick_list = [RANDOM_NUM_ONE, RANDOM_NUM_TWO, RANDOM_NUM_THREE, RANDOM_NUM_FOUR, RANDOM_NUM_FIVE,
                           RANDOM_NUM_SIX]
        print(quick_pick_list[0], quick_pick_list[1], quick_pick_list[2], quick_pick_list[3], quick_pick_list[4],
              quick_pick_list[5])


main()

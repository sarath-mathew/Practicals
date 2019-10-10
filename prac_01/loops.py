def main():
    for i in range(0, 101, 10):
        print(i, end=" ")
    print('\n')

    for j in range(20, 0, -1):
        print(j, end=" ")
    print("\n")
    #     had to look at the cheat sheet to find solution for stars
    number_of_stars = int(input("please enter the amount stars you want"))
    for k in range(1, number_of_stars + 1):
        print('*', end=" ")

    print("\n")
    number_of_stars_improved = int(input("please enter the amount stars you want"))
    for l in range(1, number_of_stars_improved + 1):
        print('*' * l)


main()

def main():
    name_file = open("name.txt", 'r+')
    name = input("please enter your name >")
    name_file.write(name)
    name = name_file.readline()
    name_file.close()
    print("Your name is {}".format(name))

    numbers_file = open('numbers.txt', 'r')
    number_one = int(numbers_file.readline())
    number_two = int(numbers_file.readline())
    numbers_file.close()
    print(number_one + number_two)


main()

try:
    numerator = int(input("Enter the numerator: "))
    while numerator == 0:
        print("please make sure the numerator or denominator is not a 0 ")
        numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("please make sure the numerator or denominator is not a 0 ")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Question 1: A ValueError will occur when the input is not the expected value, i.e a string input instead of an integer
# Quesiton 2: A ZeroDivisionError will occur when either the numerator or denominator is entered as 0, since dividing by 0 is illogical it will crash the program
# Question 3: we could integrate a while loop that does not allow the user to enter a zero, and keeps asking them to enter another value
#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to enter positive integer
# The program will add all the positive numbers up to the integer


def main():
    # this tells the user the sum of
    # all the positive numbers from the integer

    # input
    number_count = input("Please enter a positive integer: ")
    sum = 0

    # process & output
    try:
        integer_as_number = int(number_count)

        while integer_as_number > 0:
            sum = sum + integer_as_number
            integer_as_number = integer_as_number - 1

        print("The sum from all the positive numbers is {0}.".format(sum))

    except Exception:
        print("This is not a positive integer!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()

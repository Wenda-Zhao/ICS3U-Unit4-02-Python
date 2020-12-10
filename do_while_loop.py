#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program is for do while loop


def main():
    # this function is for do while loop
    basic_number = 1
    loop_number = 1

    # input
    positive_number = input("Enter a non-negative number: ")
    print("")

    # process & output
    try:
        positive_number_int = int(positive_number)
        print("It is a integer")
        if positive_number_int >= 0:
            while basic_number <= positive_number_int:
                loop_number = loop_number * basic_number
                basic_number = basic_number + 1
            print("{0}! = {1}".format(positive_number_int, loop_number))
        else:
            print("It is not a non-negative number")
    except Exception:
        print("It is not a integer")
    finally:
        print("Done!")


if __name__ == "__main__":
    main()

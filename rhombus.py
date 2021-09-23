#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate the area and perimeter of the rhombus


def main():
    # This function calculate the area and perimeter of the rhombus

    # input
    sides = int(input("Enter the side of the rhombus(cm): "))
    diagonal = int(input("Enter the diagonal of the rhombus(cm): "))
    another_diagonal = int(input("Enter the another diagonal of the rhombus(cm): "))
    print("")

    # process
    area = (diagonal * another_diagonal) / 2
    perimeter = 4 * sides

    # output
    print("a = (diagonal x anotherdiagonal) / 2 = {} cm²".format(area))
    print("p = 4 x sides = {} cm".format(perimeter))
    print("\nDone")


if __name__ == "__main__":
    main()

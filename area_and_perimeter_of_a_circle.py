# 1/usr/bin/env python3

# Created by Larry Nkengbeza
# Created on NOvember 2020
# This program is meant to calculate area and perimeter of a circel
# with a radius of 15mm
import math


def main():
    # this function calculates area and perimeter of a circle

    rad = 15
    print("If a circle has a radius of 15mm")
    print("The area is {}mm2".format(math.pi*rad**2))
    print("And the perimeter is {}mm".format(math.pi*2*rad))


if __name__ == "__main__":
    main()

# 1/usr/bin/env python3

# Created by Larry Nkengbeza
# Created on NOvember 2020
# This program is meant to calculate area and perimeter of a circel
# with a radius of 15mm


def main():
    '#this function calculates area and perimeter of a circle'
    import math
    rad = 15
    print("Area is {}cm^2".format(math.pi*rad**2))
    print("Perimeter is {}cm^2".format(math.pi*2*rad))


if __name__ == "__main__":
    main()

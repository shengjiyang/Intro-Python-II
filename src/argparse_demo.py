# argparse_demo.py

# Understanding argparse
# example: calculating the volume of a cylinder
# Cylinder Volume = pi * (r ** 2) * h

import argparse
import math

description = "Calculates the volume of a cylinder"
parser = argparse.ArgumentParser(description=description)

# Adding shorcuts -r and -H obligates the user to state the
# arguments in the command line.
parser.add_argument("-r", "--radius", type=float, help="Radius of Cylinder")
parser.add_argument("-H", "--height", type=float, help="Height of Cylinder")
args = parser.parse_args()

def cylinder_vol(radius, height):
    return math.pi * (radius ** 2) * height

if __name__ == "__main__":
    print(cylinder_vol(args.radius, args.height))
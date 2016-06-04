#!/usr/bin/python
import util

filename = raw_input("Enter the matrix filename to be analyzed : ")
util.createCoords(filename, "coord.txt")
print avgNeighbor("grid.txt")



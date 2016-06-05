#!/usr/bin/python
import util

filename = raw_input("Enter the matrix filename to be analyzed : ")
#util.createCoords(filename, "coord.txt")
anp = util.avgNeighbor("grid.txt")

a = (-0.9492 * anp) + 2.3636
b = 10**a

print "\n Best guess for kappa is : ", b

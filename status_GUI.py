#!/usr/bin/python

from Tkinter import *
from time import sleep
import util

util.createCoords("grid.txt", "coord.txt")
print "Total particles : ", util.particlesinMatrix("grid.txt")

gridSize = util.dimension("grid.txt")

def draw():
	x = 0
	y = 0
	f1 = open("coord.txt", "r")
	coords = f1.readline().split()
	print len(coords)
	r = len(coords)-2
	for i in xrange(0,r,2):
		w.create_oval(x, y, x+1, y+1, fill="white")
		x = int(coords[i])
		y = int(coords[i+1])
	numParticles = str(((r+2)/2)+1)+ "  particles "

root=Tk()
root.wm_title("DLA Simulation")
w = Canvas(root, width=gridSize, height=gridSize)
draw()
w.pack()
root.mainloop()

#!/usr/bin/python

from Tkinter import *
from time import sleep

gridSize = int(raw_input("Size of the square matrix : "))
kappa = raw_input("Enter stickiness factor kappa : ")

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
	numParticles = str(((r+2)/2)+1)+ "  particle , k = " + kappa	
	w.create_text(str(gridSize/2), str(gridSize-20), text=numParticles, fill="red", font="Helvetica 12 bold")

root=Tk()
root.wm_title("DLA Simulation")
w = Canvas(root, width=gridSize, height=gridSize)
draw()
w.pack()
root.mainloop()

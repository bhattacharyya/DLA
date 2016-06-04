#!/usr/bin/python

from Tkinter import *
from time import sleep

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
	numParticles = str((r+2/2)+1)+ "  particle , k = 1"	
	w.create_text(250, 480, text=numParticles, fill="red", font="Helvetica 12 bold")

root=Tk()
root.wm_title("DLA Simulation")
w = Canvas(root, width=501, height=501)
draw()
w.pack()
root.mainloop()
#w.after(4000, draw)

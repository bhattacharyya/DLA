#!/usr/bin/python

################################################################################
#                                                                        
#  author  : Shantanu S. Bhattacharyya                                    
#  date    : May 31, 2016
#  updated : 
#
#  This code simulates the "Diffusion Limited Aggregation" based on the
#  description written by Paul Bourke. The code is submitted as a part of
#  problem solving exercise sent to me.
#
################################################################################

from random import randint, choice

class dlagrid:
	grid = []
	index1 = 0
	index2 = 0

	def __init__(self):
		return None

	def createGrid(self): # Creating a 2D list / array
		for i in range(0,22):
			self.grid.append([])
		for j in range(0,22):
			for k in range(0,22):
				self.grid[j].append(0)
		self.grid[11][11] = 1
		
		return None

	def newParticle(self): # Introduce new particle in grid

		nonZeroCell = True
		while nonZeroCell == True:
			a = randint(0,21)
			b = randint(0,21)
			if self.grid[a][b] == 0:
				self.grid[a][b] = 1
				nonZeroCell = False
				print "Particle seeded at ", a, b
				self.index1 = a
				self.index2 = b

	def showGrid(self):
		for row in self.grid :
			print row
		return None

	def diffuse(self):
		x = randint(0,1)
		y = randint(0,1)
		z = choice([-1,1]) 

		newIndex1 = self.index1 + x*z
		newIndex2 = self.index2 + y*z

		print newIndex1, newIndex2

		self.grid[self.index1][self.index2] = 0
		self.grid[newIndex1][newIndex2] = 1

		self.index1 = newIndex1
		self.index2 = newIndex2

		return None


test = dlagrid()
test.createGrid()
test.showGrid()
test.newParticle()
test.showGrid()
print "jkdhfdjkhfd\nljksdfks\njfsgklfj"
test.diffuse()
test.showGrid()
	
# Loop over rows.
#for row in grid:
#	print row



#!/usr/bin/python

################################################################################
#                                                                        
#  author  : Shantanu S. Bhattacharyya                                    
#  date    : May 31, 2016
#  updated : June 3, 2016 
#
#  This code simulates the "Diffusion Limited Aggregation" based on the
#  description written by Paul Bourke. The code is submitted as a part of
#  problem solving exercise sent to me.
#
################################################################################

from random import randint, choice

# Resolving the stickiness coefficient
coeff = raw_input("Enter stickiness coefficient: ")
kappa = coeff.split("e-")
print kappa
kappa_int = int(kappa[0])
kappa_range = 10 ** int(kappa[1])

# Asking for grid size
grid_size = int(raw_input("Enter dimension of square matrix: "))

class dlagrid:
	grid = []
	index1 = 0
	index2 = 0
	decision = False
	enclosed = True	

	def __init__(self):
		return None

	def createGrid(self): # Creating a 2D list / array
		for i in range(0,grid_size):
			self.grid.append([])
		for j in range(0,grid_size):
			for k in range(0,grid_size):
				self.grid[j].append(0)
		self.grid[grid_size/2][grid_size/2] = 1
		
		return None

	def blankNeighbor(self): # Check if a neighboring pixel is available for move
		for n in range(-1,2):
			for p in range(-1,2):
				a = self.index1 + n
				b = self.index2 + p
				if (a,b) != (self.index1, self.index2):
					if 0 <= a <= grid_size-1 and 0 <= b <= grid_size-1 :
						if self.grid[a][b] == 0:
							self.enclosed = False
		return self.enclosed

	def newParticle(self): # Introduce new particle in grid

		nonZeroCell = True
		self.decision = False
		while nonZeroCell == True:
			sides = choice(['topbottom', 'leftright'])
			if sides == 'topbottom':
				a = choice([0,grid_size-1])
				b = randint(0,grid_size-1)
			if sides == 'leftright':
				a =  randint(0,grid_size-1)
				b = choice([0,grid_size-1])
			if self.grid[a][b] == 0:
				self.grid[a][b] = 1
				nonZeroCell = False
				self.index1 = a
				self.index2 = b

	def showGrid(self): # Displays current grid contents on screen
		for row in self.grid :
			print row
		return None

	def getGrid(self, filename): # Writes out the grid content to a file
		f1 = open(filename, 'w')
		for row in self.grid:
			f1.write("%s\n" % row)
		f1.close()
		return None

	def setValue(self,a,b,n): # Set value of point in matrix
		self.grid[int(a)][int(b)] = int(n)
		return None
	
	def isStuck(self): # Determine if a moving particle touched an existing particle
		for n in range(-1,2):
			for p in range(-1,2):
				a = self.index1 + n
				b = self.index2 + p
				if (a,b) != (self.index1, self.index2):
					if 0 <= a <= grid_size-1 and 0 <= b <= grid_size-1 :
						if self.grid[a][b] == 1:
							self.decision = True
							break

		# This part below implements the "stickiness factor"

		if self.decision == True:
			temp = randint(1,kappa_range)
			if temp > kappa_int:
				self.decision = False

		return self.decision

	def getPosition(self): # Returns position of the moving particle on the grid 
		return (self.index1 , self.index2) # (0,0 is the top left position)

	def diffuse(self): # Moves the particle by one unit in any random direction
		x = 0
		y = 0

		while (True) : 
			if self.blankNeighbor() == True:
				break

			x = choice([0,1,-1]) 
			y = choice([0,1,-1])
			if (x != 0 or y != 0): # Make sure particle is not stationary
				if self.index1 == 0 :
					x = 1
				if self.index1 == grid_size-1 :
					x = -1
				if self.index2 == 0 :
					y = 1
				if self.index2 == grid_size-1 :
					y = -1

				newIndex1 = self.index1 + x
				newIndex2 = self.index2 + y
				if self.grid[newIndex1][newIndex2] != 1:
					self.grid[self.index1][self.index2] = 0
					self.grid[newIndex1][newIndex2] = 1
		
					self.index1 = newIndex1
					self.index2 = newIndex2					
					break
		return None


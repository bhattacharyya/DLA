#!/usr/bin/python

def readMatrixFile(matrixfile): # Reads the matrix output of DLA simulation,
	f1 = open(matrixfile, "r") #      default "grid.txt"
	lines = f1.readlines()
	A = []
	for i in lines:
		row = []
		for k in list(i):
			if k in ["0","1"]:
				row.append(k)
		A.append(row)
	return A

def dimension(matrixfile): # Returns the size of the matrix
	mat = []
	f1 = open(matrixfile, "r")
	line = f1.readline().split()
	f1.close()
	return len(line)

def createCoords(matrixfile, coordfile): # Extracts cordinated of particles that the GUI can 
	limit = dimension(matrixfile)        # use to generate the simulation image
	count = 0
	f1 = open(matrixfile, "r")
	f2 = open(coordfile, "w")
	lines = f1.readlines()
	for i in lines:
		row = []
		for k in list(i):
			if k in ["0","1"]:
				row.append(k)
		for j in range(0, limit):
			if row[j] == "1":
				f2.write(str(count) + " " + str(j)+" ")
		count += 1
	f1.close()
	f2.close()
	return None
				
def particlesinMatrix(matrixfile): # Returns number of particles in the matrix
	f1 = open(matrixfile, "r")
	lines = f1.readlines()
	count = 0
	for i in lines:
		row = []
		for k in list(i):
			if k == "1":
				count += 1
	f1.close()
	return count

def minGridSize(matrixfile): # The minimum are of the grid outside which matrix is empty
	limit = dimension(matrixfile)
	edge1 = 0
	edge2 = limit-1
	index1 = ""
	index2 = ""
	M = readMatrixFile("grid.txt")
	while(index1 == ""):
		for i in range(0,limit):
			if M[i][edge1] == "1":  
				index1 = edge1
				break
			if M[i][edge2] == "1":
				index1 = edge2
				break
		edge1 += 1
		edge2 -= 1
	
	edge1 = 0
	edge2 = limit-1

	while(index2 == ""):
		for k in range(0,limit):
			if M[edge1][k] == "1":
				index2 = edge1
				break
			if M[edge2][k] == "1":
				index2 = edge2
				break
		edge1 += 1
		edge2 -= 1
	
	(a,b) = 2*abs((limit/2)-(index1)), 2*abs((limit/2)-(index2))
	side1 = a+1
	side2 = b+1
	area = side1 * side2
	return abs(area)

def particlesAround(matrixfile, row, column): # Returns how many particles are neighboring the given particle
	M = readMatrixFile(matrixfile)
	count = 0
	limit = dimension(matrixfile)
	for n in range(-1,2):
		for p in range(-1,2):
			a = int(row) + n
			b = int(column) + p
			if (a,b) != (row, column):
				if 0 <= a <= limit-1 and 0 <= b <= limit-1 :
					if M[a][b] == "1":
						count += 1
	
	return count

def avgNeighbor(matrixfile): # Average number of particles that any particle has in the grid
	print "\nAnalyzing grid ... \n"
	M = readMatrixFile(matrixfile)
	count = 0
	limit = dimension(matrixfile)
	for i in range(0, limit):
		if i % 5 == 0:
			print "row " + str(i) + " analyzed"
		for j in range(0, limit):
			if M[i][j] == "1":
				count += particlesAround(matrixfile, i, j)
	avg = float(count) / particlesinMatrix(matrixfile)
	return avg
	

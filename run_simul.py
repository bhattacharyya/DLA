#!/usr/bin/python

import dla_simul

totalParticles = int(raw_input("Total particles to simulate"))
count = 0

test = dla_simul.dlagrid()
test.createGrid()

for k in range(1,totalParticles+1):
	count += 1
	test.newParticle()
	while test.isStuck() == False :
		test.diffuse()

	print "Particle number : " + str(count) 
	if count % 1000 == 0:
		test.getGrid("grid.txt")

test.showGrid()

test.getGrid("grid.txt")

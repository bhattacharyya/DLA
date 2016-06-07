#!/usr/bin/python

import dla_simul

count = 0

test = dla_simul.dlagrid()
test.createGrid()

tenpercent = test.numberOfParticles()/10
for k in range(1,test.numberOfParticles()+1):
	count += 1
	test.newParticle()
	while test.isStuck() == False :
		test.diffuse()

	if count % tenpercent == 0:
		print str(count) + " particles done"
		test.getGrid("grid.txt")

test.showGrid()

print "\nSimulation Over ; matrix output as grid.txt \n"

test.getGrid("grid.txt")

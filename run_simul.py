#!/usr/bin/python

import dla_simul

totalParticles = int(raw_input("Total particles to simulate : "))
fivepercent = totalParticles/5
count = 0

test = dla_simul.dlagrid()
test.createGrid()

for k in range(1,totalParticles+1):
	count += 1
	test.newParticle()
	while test.isStuck() == False :
		test.diffuse()

	if count % fivepercent == 0:
		print str(count) + " particles done"
		test.getGrid("grid.txt")

test.showGrid()

print "\nSimulation Over ; matrix output as grid.txt \n"

test.getGrid("grid.txt")

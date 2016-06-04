#!/usr/bin/python

import dla_simul
count = 0
x = 250
y = 250
coords = []

test = dla_simul.dlagrid()
test.createGrid()

for k in range(1,501):
	count += 1
	test.newParticle()
	while test.isStuck() == False :
		#count += 1
		test.diffuse()
	(a,b) = test.getPosition()
	coords.append(a)
	coords.append(b)
	coordfile = open("coord.txt", "w")
	for i in list(coords):
		coordfile = open("coord.txt", "a")
		coordfile.write(str(i) + " ")
		coordfile.close()



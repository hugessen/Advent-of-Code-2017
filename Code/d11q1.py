pinput = open("../Inputs/d11.txt").read().split(",")
x = 0
y = 0
z = 0
largest = 0
print pinput
for p in pinput:
	if p == "n":
		x += 1
		z -= 1
	elif p == "ne":
		x += 1
		y -= 1
	elif p == "nw":
		y += 1
		z -= 1
	elif p == "s":
		z += 1
		x -= 1
	elif p == "se":
		z += 1
		y -= 1
	elif p == "sw":
		y += 1
		x -= 1
	if (abs(x) + abs(y) + abs(z)) / 2 > largest:
		largest = (abs(x) + abs(y) + abs(z)) / 2
print "x: %d y: %d z: %d" % (x,y,z)
print (abs(x) + abs(y) + abs(z)) / 2
print largest
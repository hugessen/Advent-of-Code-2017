input = open("Inputs/d2q1.txt")

def check_divisible(x1,x2):
	larger = 0
	smaller = 0
	if x1 > x2: 
		larger = x1
		smaller = x2
	elif x1 < x2:
		larger = x2
		smaller = x1
	else:
		return -1
	if larger % smaller == 0:
		return larger / smaller
	else:
		return -1

def find_pair(numbers):
	for i in range(0, len(numbers)):
		for j in range(i, len(numbers)):
			res = check_divisible(numbers[i],numbers[j])
			if res is not -1:
				return res
	return -1

line = input.readline()
checksum = 0

while line:
	numbers = map(int,line.split())
	pair = find_pair(numbers)
	if pair is not -1:
		checksum += pair
	else:
	  print "Error"
	line = input.readline()
print checksum

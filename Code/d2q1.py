input = open("Inputs/d2q1.txt")

def sum_line(numbers_line):
	numbers = map(int,numbers_line.split())
	min = 10000000
	max = 0
	for i in range (0,len(numbers)):
		if (numbers[i] < min):
			min = numbers[i]
		if (numbers[i] > max):
			max = numbers[i]
	return max - min

line = input.readline()
checksum = 0

while line:
	checksum += sum_line(line)
	line = input.readline()

print checksum
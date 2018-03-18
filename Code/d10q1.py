pinput = open("../Inputs/d10.txt").read().split(",")
pinput = map(int,pinput)

numbers = []
for i in range(0, 256):
	numbers.append(i)

ind = 0
skip = 0
nums_len = len(numbers)

def reverse(start,end, length):
	for i in range(0, length / 2):	
		temp = numbers[start]
		numbers[start] = numbers[end]
		numbers[end] = temp

		if start < nums_len - 1:
			start += 1
		else:
			start = 0

		if end > 0:
			end -= 1
		else:
			end = nums_len - 1

for length in pinput:
	if length > nums_len - ind:
		reverse(ind, ind + length - nums_len - 1, length)
	else:
		reverse(ind, ind + length - 1, length)
	if length + skip > nums_len - ind:
		ind = ind + length - nums_len
		if ind + skip > nums_len:
			ind = ind + skip - nums_len
		else:
			ind = ind + skip
	else:
		ind = ind + length + skip
	skip += 1

print numbers
print numbers[0] * numbers[1]
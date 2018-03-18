def redistribute(blocks):
	fullest = 0
	for x in range(0,len(blocks)):
		if blocks[x] > blocks[fullest]:
			fullest = x
	memory = blocks[fullest]
	blocks[fullest] = 0
	if fullest == len(blocks) - 1:
		i = 0
	else:
		i = fullest + 1

	while memory > 0:
		blocks[i] += 1
		if i == len(blocks) - 1:
			i = 0
		else:
			i += 1
		memory -= 1
	return blocks

def matches_previous(curr,previous_states):
	for i in range (0,len(previous_states)):
		if previous_states[i] == curr:
			print i
			return True
	return False

blocks = open("../Inputs/d6q1.txt").readline().split()
blocks = map(int,blocks)

count = 1
previous_states = [blocks[:]]
blocks = redistribute(blocks)
print previous_states[0]
print blocks

while not matches_previous(blocks, previous_states):
	previous_states.append(blocks[:])
	blocks = redistribute(blocks)
	count += 1
print count
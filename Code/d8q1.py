data = open("../Inputs/d8q1.txt")

registers = {}
line = data.readline()

def check_cond(cond):
	if cond[0] not in registers:
		name = cond[0]
		registers[name] = 0

	if cond[1] == "<":
		return registers[cond[0]] < int(cond[2])
	if cond[1] == ">":
		return registers[cond[0]] > int(cond[2])
	if cond[1] == "<=":
		return registers[cond[0]] <= int(cond[2])
	if cond[1] == ">=":
		return registers[cond[0]] >= int(cond[2])
	if cond[1] == "==":
		return registers[cond[0]] == int(cond[2])
	if cond[1] == "!=":
		return registers[cond[0]] != int(cond[2])

largest = 0
while line:
	line = line.split()
	if line[0] not in registers:
		registers[line[0]] = 0
	if check_cond(line[4:]):
		if line[1] == "inc":
			registers[line[0]] += int(line[2])
		if line[1] == "dec":
			registers[line[0]] -= int(line[2])
	if registers[line[0]] > largest:
		largest = registers[line[0]]
	line = data.readline()

print largest
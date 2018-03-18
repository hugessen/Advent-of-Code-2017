data = open("../inputs/d7q1.txt")

child_programs = []
all_programs = []
line = data.readline()

while line:
	line = line.split()
	all_programs.append(line[0])
	if "->" in line:
		i = line.index("->") + 1
		while i < len(line):
			child_programs.append(line[i].replace(",",""))
			i += 1
	line = data.readline()

for prog in all_programs:
	if child_programs.index(prog) == -1: #Prints an error lol
		print prog
		break
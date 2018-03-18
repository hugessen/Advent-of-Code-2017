pinput = open("d9.txt").read()

level = 0
total = 0
garbage = False
i = 0

while i < len(pinput):
	if not garbage:
		if pinput[i] == "{":
			level += 1
		elif pinput[i] == "}":
			level -= 1
		elif pinput[i] == "<":
			garbage = True
	else:
		if pinput[i] == "!":
			i += 1
		elif pinput[i] == ">":
			garbage = False
		else:
			total += 1
	i += 1
print total
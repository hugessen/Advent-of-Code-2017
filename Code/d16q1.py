def spin(x):
	end = len(bros) - x
	val = "" + bros[-x:] + bros[:end]
	return val

def swap(a, b):
	val = list(bros)
	val[a], val[b] = val[b], val[a]
	return "".join(val)

def partner(a, b):
	a = bros.find(a)
	b = bros.find(b)
	return swap(a, b)

def do_dance(dance):
	if dance[0] == "s":
		bros = spin(int(dance[1:]))
	elif dance[0] == "x":
		vals = dance[1:].strip("\n").split("/")
		bros = swap(int(vals[0]),int(vals[1]))
	elif dance[0] == "p":
		vals = dance[1:].strip("\n").split("/")
		bros = partner(vals[0], vals[1])

# njfgilbkcoemhpad
bros = "abcdefghijklmnop"
initial = "abcdefghijklmnop"
iterations = 100062819
i = 0
while i < iterations:
	if bros == initial:
		i += (iterations / (1 + 1) - 1) * (i + 1)
	pinput = open("../Inputs/d16.txt").read().split(",") 
	for dance in pinput:
		do_dance(dance)
	i += 1
print bros
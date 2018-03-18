#hlhomy
#tknk
data = open("../inputs/d7q1.txt")
line = data.readline()
lines = []
progs = {}
root = "hlhomy"

def get_children(node):
	c = progs[node][0]
	if len(c) == 0:
		return progs[node][1] #No children; return weight
	else:
		return c

def r_weight(node):
	children = get_children(node)
	if type(children) is int: 
		return children

	weight = 0
	for child in children:
		weight += r_weight(child)
	return weight + progs[node][1]

def get_errant_node(nodes):
	if len(set(nodes)) == 1:
		return -1

	if nodes.count(nodes[0]) > 1:
		proper = nodes[0]
	else:
		return 0

	for i in range(0,len(nodes)):
		if nodes[i] != proper:
			return i

def get_faulty_node_r(root):
	kiddos = get_children(root)
	kid_weights = []
	for kid in kiddos:
		kid_weights.append(r_weight(kid))

	ind = get_errant_node(kid_weights)
	if ind == -1: #In that moment, I realized I was the problem...
		print "Problem is %s with weight %d" % (root, progs[root][1])
	else:
		print "children of %s with weights:"
		print kid_weights
		get_faulty_node_r(kiddos[ind])

while line:
	line = line.split()
	lines.append(line)
	prog = line[0]
	line[1] = line[1].replace("(","")
	weight = int(line[1].replace(")",""))

	children = []
	if "->" in line:
		i = line.index("->") + 1
		while i < len(line):
			children.append(line[i].replace(",",""))
			i += 1

	progs[prog] = (children, weight)
	line = data.readline()

print get_faulty_node_r(root)
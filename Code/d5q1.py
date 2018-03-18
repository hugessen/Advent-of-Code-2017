values = [line.rstrip('\n') for line in open('richard.txt')]
values = map(int,values)
i = 0
count = 0

while i >= 0 and i < len(values):
	temp = i
	i += values[i]
	if values[temp] > 2:
		values[temp] -= 1
	else:
		values[temp] += 1
	count += 1

print "count %d" % count
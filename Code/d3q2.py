from d3q1 import *
value = 361527

def radius(number):
	i = 1
	while i**2 < number:
		i += 1
	return i / 2

def get_neighbours(index):
	if i == 4:
		return (3,2,1)
	if i == 6:
		return (5,4,1)
	if i == 9:
		return (8,2,1)
	if i == 11:
		return (10,9,2,3)
	r = radius(index)
	# First number on outer layer
	if index == first_number_on_outer_layer(r):
		return (index - 1, first_number_on_outer_layer(r -1))

	dist = get_distance_from_center(index)[0]
	cardinality = get_distance_from_center(index)[1]

	#Corner
	if (dist == r * 2):
		if cardinality == "North-West":
			return (index - 1, north(r-1) + (r-1))
		elif cardinality == "South-East":
			return (index - 1, south(r-1) + (r-1), first_number_on_outer_layer(r))
		elif cardinality == "North-East":
			return (index - 1, east(r-1) + (r-1))
		elif cardinality == "South-West":
			return (index - 1, west(r-1) + (r-1))

	nearest_cardinality = get_nearest_cardinality(cardinality,r)

	dist_from_nearest_cardinality = index - nearest_cardinality
	# 1 less than corner
	if (index == nearest_cardinality + r - 1) and cardinality is not "South":
		return (index - 1, get_nearest_cardinality(cardinality, r - 1) + (r - 1), get_nearest_cardinality(cardinality, r - 1) + (r-2))
	elif (index == nearest_cardinality - (r - 1)) and cardinality is not "East":
		return (index -1, index - 2, get_nearest_cardinality(cardinality, r - 1) + dist_from_nearest_cardinality, get_nearest_cardinality(cardinality, r - 1) + dist_from_nearest_cardinality + 1)

	return (index -1, get_nearest_cardinality(cardinality, r - 1) + dist_from_nearest_cardinality - 1, get_nearest_cardinality(cardinality, r - 1) + dist_from_nearest_cardinality, get_nearest_cardinality(cardinality, r - 1) + dist_from_nearest_cardinality + 1)

def first_number_on_outer_layer(r):
	return (r*2 - 1)**2 + 1

def north(r):
	return (r * 2)**2 - (r - 1)

def south(r):
	return (r * 2 + 1)**2 - r

def east(r):
	return (r * 2 - 1)**2 + r

def west(r):
	return (r * 2)**2 + r + 1

def get_nearest_cardinality(cardinality, r):
	if cardinality == "North":
		return north(r)
	elif cardinality == "South":
		return south(r)
	elif cardinality == "East":
		return east(r)
	elif cardinality == "West":
		return west(r)


grid = [0,1,1]
i = 3

while grid[i - 1] < value:
	neighbours = get_neighbours(i)
	total = 0
	for neighbour in neighbours:
		total += grid[neighbour]
	grid.append(total)
	print total
	i += 1
# print r

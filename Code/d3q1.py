value = 361527
answer = -1

def radius(number):
	i = 1
	while i**2 < number:
		i += 1
	return i / 2

def get_distance_from_center(value):
	r = radius(value)
	north = (r * 2)**2 - (r - 1)
	east = (r * 2 - 1)**2 + r
	south = (r * 2 + 1)**2 - r
	west = (r * 2)**2 + r + 1

	if value <= east:
		if value < east:
			answer = r + (value - east)
			closest_to = "East"
		elif (value == east):
			answer = r
			closest_to = "East"
		
	if (value >= south):
	 	if value > south:
	 		if value == (r * 2 + 1)**2:
	 			answer = r * 2
	 			closest_to = "South-East"
 			else:
 				answer = r
 				closest_to = "South"
		elif value == south:
			answer = r
			closest_to = "South"

	elif (value <= north):
		if value - east > north - value:
			answer = r + (north - value)
			closest_to = "North"
		elif value - east < north - value:
			answer = r + (value - east)
			closest_to = "East"
		elif (value == north):
			answer = r
			closest_to = "North"
		else:
			answer = r*2
			closest_to = "North-East"

	elif (value <= west):
		if value - north > west - value:
			answer = r + (west - value)
			closest_to = "West"
		elif value - north < west - value:
			answer = r + (value - north)
			closest_to = "North"
		elif (value == west):
			answer = r
			closest_to = "West"
		else:
			answer = r*2
			closest_to = "North-West"

	elif (value < south):
		if value - west > south - value:
			answer = r + (south - value)
			closest_to = "South"
		elif value - west < south - value:
			answer = r + (value - west)
			closest_to = "West"
		else:
			answer = r*2
			closest_to = "South-West"

	return (answer, closest_to)

print get_distance_from_center(value)[0]
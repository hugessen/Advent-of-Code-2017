a_factor = 16807
b_factor = 48271
mod_factor = 2147483647
a = 699
b = 124
total = 0

def next_gen(a,b):
	a = (a * a_factor) % mod_factor
	b = (b * b_factor) % mod_factor
	return (a,b)

def matches_pair(a,b):
	return bin(a)[-16:] == bin(b)[-16:]

for i in range(0,40000000):
	a,b = next_gen(a,b)
	if matches_pair(a,b):
		total += 1
print total
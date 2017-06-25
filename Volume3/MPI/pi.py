import random

n = 100000
s = 0

for i in range(n):
	x = random.uniform(-1.0,1.0)
	y = random.uniform(-1.0,1.0)
	
	if x**2 + y**2 <= 1:
		s += 1

print 4.0*s/n

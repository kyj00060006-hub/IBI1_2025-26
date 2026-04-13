# What does this piece of code do?
# Answer: run the While loop for 11 times, every time it generate an random integer bwtween 1 and 10, accumulates the sum, and prints the total.
# and i think 'ceil' is useless.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

print(total_rand)


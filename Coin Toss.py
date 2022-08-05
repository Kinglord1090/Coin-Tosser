# Imports
import random

# Variables
number_of_flips = int(input("Enter the number of times you want to flip the coin: "))
sides = ["Heads", "Tails"]
sequence = []
count = {"Heads": 0, "Tails": 0}

# Solver
for flip in range(number_of_flips):
	result = random.choice(sides)
	if result == "Heads":
		sequence.append("H")
		count["Heads"] += 1
	else:
		sequence.append("T")
		count["Tails"] += 1

print(sequence)
print(count)

import random


number_of_flips = int(input("Enter the number of times you want to flip the coin: "))
sequence = []
count = {"Heads": 0, "Tails": 0}


for flip in range(number_of_flips):
	result = random.randrange(2)
	if result == 0:
		sequence.append("H")
		count["Heads"] += 1
	else:
		sequence.append("T")
		count["Tails"] += 1

print(sequence)
print(count)

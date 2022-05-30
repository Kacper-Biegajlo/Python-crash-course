import matplotlib.pyplot as plt
import numpy as np

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1): 
    frequency = results.count(value)
    frequencies.append(frequency)

plt.hist(results, bins=np.arange(2, die.num_sides+2)-.5, histtype = 'bar', 
         rwidth=0.8, facecolor = 'blue', edgecolor="k")

plt.title("Dice Plot")
plt.xlabel("Results")
plt.ylabel("Frequency of Result")

plt.show()

#this took me a lot of time, from my understanding matplotlib is not made for this
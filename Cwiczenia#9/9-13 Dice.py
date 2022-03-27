## -13. Dice: 
# 
# Make a class Die with one attribute called sides, which has a default value 
#   of 6. 
# 
# Write a method called roll_die() that prints a random number between 1 and 
#   the number of sides the die has. 
# 
# Make a 6-sided die and roll it 10 times.
# 
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

class Dice:
    """Class for portraying a dice."""
    def __init__(self, sides):
        """Choosing number of sides for dice, normally it is 6."""
        self.sides = sides

    def roll_die(self, times):
        """Rolling the dice!"""
        self.times = times
        from random import randint
        for time in range(self.times):
            print(randint(1,self.sides))

# Rollind d6 10 times
d6 = Dice(6)
print("Results:")
d6.roll_die(10)


# Roling d10 10 times
d10 = Dice(10)
print("\nResults:")
d10.roll_die(10)

# Rolling d20 10 times
d20 = Dice(20)
print("\nResults:")
d20.roll_die(10)


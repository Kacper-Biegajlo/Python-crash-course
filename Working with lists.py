### WORKING WITH LISTS ###

# Doing More Work Within a for Loop

print("\n\t"+"Doing More Work Within a for Loop"+"\n")

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: # loop that assigns variable with each element from the list one by one then prints it
    print(magician)

print("\t")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("\t")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
       print(f"{magician.title()}, that was a great trick!")
       print(f"I can't wait to see your next trick, {magician.title()}.\n")


# Doing Something After a for Loop

print("\n\t"+"Doing Something After a for Loop"+"\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
       print(f"{magician.title()}, that was a great trick!")
       print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!") # summery of the loop outside of it

# Forgetting to Indent

print("\n\t"+"Forgetting to Indent"+"\n")

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

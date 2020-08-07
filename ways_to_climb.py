# There exists a staircase with N steps,
# and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of
# unique ways you can climb the staircase. The order
# of the steps matters.

steps = 4

def how_many_ways(s):
    if (s == 1):
        return 1
    if (s == 2):
        return 2 
    # for all s > 2, we add the previous (s - 1) + (s - 2) steps to get
    # an answer recursively
    return how_many_ways(s - 1) + how_many_ways(s - 2)

print("Total ways: ", how_many_ways(steps))
    
    

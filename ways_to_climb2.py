# There exists a staircase with N steps,
# and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of
# unique ways you can climb the staircase. The order
# of the steps matters.

steps = 4

def how_many_ways(steps):
  total = 1

  for i in range(2,steps+1):
    total += how_many_ways(steps - i)
    
  return total


print("Total ways: ", how_many_ways(steps))
    
    

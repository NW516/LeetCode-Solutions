# The problem: Find the missing number in a
# given array of integers 1 to 100

ints = [1,2,3,4,5,6,7,8,9,11]
for i in range(1,12):
    if i in ints:
        print(i)
    else:
        print(f"{i} not in array")

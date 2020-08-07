# The problem: Given an array of integers, return a 
# new array such that each element at index i of the
# new array is the product of all the numbers in the
# original array *except* the one at i.

array_of_ints = [2,3,4,5,6]
new_array = []

for i in range(len(array_of_ints)):
    new_array.append(1)
    for j in range(len(array_of_ints)):
        if i != j:
            new_array[i] *= array_of_ints[j] 
    print("New array value is: ", new_array[i])
          

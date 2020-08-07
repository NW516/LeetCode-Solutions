# The problem: Given an array of integers, return a 
# new array such that each element at index i of the
# new array is the product of all the numbers in the
# original array *except* the one at i.

array_of_ints = [2,3,4,5,6]
new_array = []

# Iterate through each element of the original array of integers 
for i in range(len(array_of_ints)):

    # Initialize each element of the new array to 1
    # (NOT zero because you're going to be multiplying!)
    new_array.append(1)

    # For each element in the original array,
    # you're going to iterate through the whole array AGAIN,
    # to handle the multiplication
    for j in range(len(array_of_ints)):
        
        # Remember, you want the product of all elements
        # EXCEPT the current element. That's why you test if i != j 
        if i != j:
            # this means "new_array[i] = new_array[i] * array_of_ints[j]
            new_array[i] *= array_of_ints[j] 
    print("New array value is: ", new_array[i])
          

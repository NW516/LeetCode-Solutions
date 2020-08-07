# The problem: Find the symmetric difference
# between two arrays.

array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]

set1 = set(array1) - set(array2)
set2 = set(array2) - set(array1)

solution = set.union(set1, set2)

print(solution)

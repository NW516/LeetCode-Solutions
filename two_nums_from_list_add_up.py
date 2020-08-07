from itertools import permutations

# The problem: Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.

num_list = [11, 15, 3, 6]
k = 17

perms = list(permutations(num_list))
msg = "No match"

for perm_tuple in perms:
    if perm_tuple[0] + perm_tuple[1] == k:
        msg = f"Success: {perm_tuple[0]}  + {perm_tuple[1]} = {k}"
        break

print(msg)

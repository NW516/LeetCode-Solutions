# Print a given integer in expanded form

import sys

digits = list(sys.argv[1])
num_length = len(digits)
print(num_length)
expanded_form = ""

for n in range(num_length-1,-1,-1) :
    print("digit: ")
    print(digits[(num_length-1)-n])
    print("num_length - 1: ")
    print(num_length - 1)
    print("n: ")
    print(n)
    this_num = int(digits[(num_length-1)-n]) * (10**n)
    print("this num: ")
    print(this_num)
    expanded_form += str(this_num)
    expanded_form += " + "

print(expanded_form)

# Given an integer, write a function to determine if it is a power of three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while (n > 1.0):
            x = n/3
            print(x)
            n = x
        if (n == 1):
            return True
        else:
            return False
        

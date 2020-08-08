# Given a non-empty array of integers, every element
# appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime
# complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ctr = dict()
        for num in nums:
            if (num in ctr):
                ctr[num] = 1
            else:
                ctr[num] = 0
        for key, value in ctr.items():
            if (value == 0):
                return key

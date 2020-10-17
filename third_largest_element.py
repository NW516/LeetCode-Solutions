# Given a non-empty array of integers, return the third
# maximum number in this array. If it does not exist,
# return the maximum number. The time complexity must be in O(n).

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_array = sorted(set(nums), reverse=True)
        if len(sorted_array)<=2:
            return sorted_array[0]
        else:
            return sorted_array[2]

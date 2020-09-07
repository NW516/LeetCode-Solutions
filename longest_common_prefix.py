# Write a function to find the longest common prefix string
# amongst an array of strings.
# If there is no common prefix, return an empty string ""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_list = list(sorted(strs, key = len))
        longest= ""
        if (sorted_list == []):
            return ""
        if (len(sorted_list) == 1):
            return(sorted_list[0])
        for i in range(len(sorted_list[0])):
            match = False
            for strng in sorted_list[1::]:
                if (strng[i] == sorted_list[0][i]):
                    match = True
                else:
                    match = False
                    return(longest)
            if (match == True):
                longest = longest + strng[i]

        return(longest)

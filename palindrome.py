# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty
# string as valid palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        lstring = s.lower()
        alphanumeric_filter = filter(str.isalnum, lstring)
        alphanumeric_string = "".join(alphanumeric_filter)
        rev_string = alphanumeric_string[::-1]
        if (alphanumeric_string == rev_string):
            return True
        else:
            return False

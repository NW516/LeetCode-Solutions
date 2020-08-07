# You are given a string S containing alphanumeric characters.
# Find out whether the string is a palindrome or not.
# Note: Consider alphabets and numbers ONLY for palindrome check.
# Ignore symbols and whitespaces.

string1 = "bob"
string2 = "john"
string3 = "ab!?ba"

def is_palindrome(s):
    s_orig = []
    for i in range(len(s)):
        if s[i].isalnum():
            s_orig.append(s[i])    
    ''.join(s_orig)
    s_rev = s_orig[::-1]
    print(s_orig)
    if s_orig == s_rev:
        return "TRUE"
    else:
        return "FALSE"

print(is_palindrome(string1))
print(is_palindrome(string2))
print(is_palindrome(string3))

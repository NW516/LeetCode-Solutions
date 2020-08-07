# Given a String of length S, reverse the whole string
# without reversing the individual words in it. Words are separated by dots.
# Example:
# Input:
# i.like.this.program.very.much
# Output:
# much.very.program.this.like.i

input_string = "my.name.is.nicole"

def reverse_words_in_string(orig_string):
    words = orig_string.split(".")
    rev_words = words[::-1]
    s = "."
    s = s.join(rev_words)
    return s

print(reverse_words_in_string(input_string))   

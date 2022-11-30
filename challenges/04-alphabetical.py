# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
str = input('enter word:')

word = list(str)
word.sort()
rearranged_word = ''.join(word)

print(rearranged_word) 
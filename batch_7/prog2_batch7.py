# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
# string to be used 
sample_word = "Hello_world.txt"

# list that contains the seperated string
words = [x for x in sample_word.split('.')]

# remove the suffix
words.remove('txt')

# print new word with the removed suffix
print(*words)
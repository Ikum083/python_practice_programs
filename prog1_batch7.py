# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
# sample string with spaces at the end of the string
sample_word = "Hello World          "

# function to split the string and remove the spaces
words = sample_word.split()

# call function 
print(*words, sep = " ")
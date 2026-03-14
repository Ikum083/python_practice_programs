# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
# sample string to be used
sample_word = "Hello word"

# prefix word to be used
prefix_word = "Hello"

# list that contains the seperated words from the sample list
words = [x for x in sample_word.split()]

# condition to check if first element from words list is the same as the prefix word
if prefix_word == words[0]:
    # print result
    print("True")
else:
    print("False")

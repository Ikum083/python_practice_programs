# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
# sample string to be used
sample_word = "Hello World"

# parameter char to be used
parameter_used = 'l'

# function to mimick count()
def iteration_count(word_used, char_used) -> int:
## list that contains every char in the string
    characters = [x for x in word_used]
## integer variable to count iterations
    count = 0
## for loop to count every iteration of the parameter in the word
    for i in characters:
        if i == char_used:
            count += 1
        else:
            continue

    return count

# call function
num_iteration = iteration_count(sample_word, parameter_used)

# print result
print(num_iteration)
# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
# string to be used
sample_word = "hello world"

# function to seperate the string and capitalize each word
def proper_case(word_used):
    # list to contain every word
    word_list = word_used.split()
    for i in range(len(word_list)):
        capitalized_word = word_list[i].capitalize()
        word_list[i] = capitalized_word
    # print new word
    print(*word_list, sep = ' ')

proper_case(sample_word)
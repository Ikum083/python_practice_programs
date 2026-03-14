# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
# string to be used
full_name = "Eugene Mabansag"

# word to be checked
end_word = "Mabansag"

# list to store the seperated words
seperated_word = []

# function to seperate string
seperated_word = full_name.split()

# condition to check if the last string is the word to be checked
if seperated_word[-1] == end_word:
    # print result
    print("True")
else:
    print("False")
# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
# string to be used
sample_word = "HeLlO wOrD"

# function to turn every lower case character to upper case and vice versa
def reverse_case(word_used):
    # list to contain all characters in the string
    character_list = []
    for i in word_used:
        if 'a' <= i <= 'z':
            character_list.append(chr(ord(i) - 32))
        elif 'A' <= i <= 'Z':
            character_list.append(chr(ord(i) + 32))
        else:
            character_list.append(i)
    print(*character_list, sep = '')

# call function
reverse_case(sample_word)
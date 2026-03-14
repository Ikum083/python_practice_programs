# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
# sample integer to be used
sample_number = 36

# desired length
desired_length = 6

# function to add zeroes at the beginning of the integer to meet desired length
def zero_fill(numbers_used, length):
    ## list of every digit in the sample integer  
    digits = list(map(int, str(numbers_used)))
    ## added while loop to keep adding 0 to meet desired length
    while len(digits) != length:
        digits.insert(0, 0)
    else:
        ## print result
        print(*digits, sep = '')

# call function
zero_fill(sample_number, desired_length)   
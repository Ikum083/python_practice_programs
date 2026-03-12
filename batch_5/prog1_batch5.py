# have user input multiple empty spaces before their name
name = str(input("Enter multiple empty spaces before you name: "))

# join the words in the name to one full name
new_name = " ".join(name.split())

# print output
print(new_name)
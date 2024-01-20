# Write a program to accept a string from the user and display characters that are present at an even index number.

# pseudocode

# accept a string from the user
string = input("Enter a word: ")

# print the string
print("Original string is", string)

# write a message printing only the even index characters
print("Printing only the even index characters")

# write a for loop to iterate through the string
for i in range(1, len(string), 2):
    # print the characters at even index numbers
    print(string[i])

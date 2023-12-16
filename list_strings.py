# Get user input for the list of strings
user_input = input("Enter a list of strings separated by spaces: ")

# Split the input into a list of strings
lw = user_input.split()

# Print the length of the list
print(f"Number of strings: {len(lw)}")

# Print the length of each string
for word in lw:
  print(f"Length of '{word}': {len(word)}")


# Open a file for writing (creates the file if it doesn't exist)
file = open("chuks.txt", "w")

# Write content to the file
file.write("Hello, this is a sample text.")
file.close()  # Close the file

# Open the file for reading
file = open("chuks.txt", "r")

# Read and print the file content
#content = file.read()
#print(content)

# Close the file
file.close()
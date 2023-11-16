
### 1. Opening a File:

# Syntax: open(file, mode)
# 'file' is the name of the file, and 'mode' specifies the purpose (read, write, append, etc.)

# Example:
file_path = 'example.txt'
file = open(file_path, 'r')  # Opens the file in read mode


### 2. Reading from a File:

# Reading the entire file content
content = file.read()
print(content)

# Reading a specific number of characters
partial_content = file.read(100)
print(partial_content)


### 3. Writing to a File:


# Writing to a file
output_text = "Hello, this is a sample text."
output_file = open('output.txt', 'w')
output_file.write(output_text)
output_file.close()

### 4. Appending to a File:


# Appending to a file
additional_text = "\nThis is additional content."
output_file = open('output.txt', 'a')
output_file.write(additional_text)
output_file.close()


### 5. Closing a File:

file.close()


### 6. Using 'with' Statement:

with open('example.txt', 'r') as file:
    content = file.read()
    # perform operations on the content

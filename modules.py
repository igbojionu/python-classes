import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password

# Example: Generate a random 12-character password
password = generate_password(30)
print(password)



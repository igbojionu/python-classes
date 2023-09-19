# Define the staff dictionary
staff = {
   'name': 'Japu',
   'phone': '+2348033428077',
   'password': 'Japu7',
   'City': 'Port Harcourt'
}

# Initialize variables
attempts = 0
max_attempts = 5

# Main login loop
while attempts < max_attempts:
    # Get user input for the password
    user_input = input("Enter your password: ")

    # Check if the entered password is correct
    if user_input == staff["password"]:
        print("Login successful!")
        break
    else:
        print("Incorrect password. Please try again.")
        attempts += 1

# Check if the maximum login attempts have been reached
if attempts == max_attempts:
    print("Maximum login attempts reached. You can no longer login.")

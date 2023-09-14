#Python while Loop:
#A while loop in Python is used when you want to repeat a block of code as long 
#as a condition is True. It's like saying, "Keep doing this until something changes."

#Example: Countdown
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

#Example: User Input Validation

user_input = ""

while user_input != "quit":
    user_input = input("Enter a command (or 'quit' to exit): ")
    print("You entered:", user_input)

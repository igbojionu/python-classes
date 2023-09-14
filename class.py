DOB = 1989
CD = 2023
age = CD - DOB
print(age)
      
items = [1, 'mango' , 2, 'grape', 3, 'orange' ]
print(items)

print('hey i am Jaja and i am', age, 'and i love', items[1])
print(f'hey i am Jaja and i am {age} and i love {items[1]}')


staff ={ 'name':'Jaja',
        'age':34,
        'phone number' : 2348034912349,

}
print (staff['phone number'])

name = 'Jaja'
age = 34
city = 'Port harcourt'

print (f'my name is {name}, i am {age} years old and i live in {city}')


username = 'Jaja'
username2 = 'Omi'
password = 1989
pwd2 = 1999

if (password == password)and (username ==username):
    print ("welcome youre logged in")
else:
    print('not coreect enter password')
    print('user name is wrong')



    # Python program for simple calculator
 
# Function to add two numbers
def add(num1, num2):
    return num1 + num2
 
# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
 
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")





 

num = int(input("enter a numnber:"))
mod = num % 2
if mod >= 2:
    print("this is an odd number")
else:
    print("this ia an even number")





 #Generate any test parameter that will test above 5 Subjects (elifs)


course1 = int(input("enter score of course1"))
course2 = int(input("enter score of course2"))
course3 = int(input("enter score of course3"))
course4 = int(input("enter score of course4"))
course5 = int(input("enter score of course5"))

if (course1 >= 80):
    print("A")
elif(course2 < course1):
    print("B")
elif(course3 < course2):
    print("C")
elif(course4 < course3):
    print("D")
elif(course5 < course4):
    print("E")



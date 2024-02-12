import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [x**2 for x in numbers]
print(numbers)

randomNumber = str(random.randint(1, 10))
fruits=["Apple", "Banana", "ChErry", "KiWi", "Mango"]
fruits = [x.lower() for x in fruits]
fruits = [x+randomNumber for x in fruits]
for fruit in fruits:
  print(fruit)

##########################################################################
#Averge height of a class
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
total_students = 0
for x in  student_heights:
  total_height += x
  total_students += 1
average_height = round(total_height / total_students)
print(f"total height = {total_height}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")
##########################################################################
# Get the highest score in a list using for loops
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
Highest = 0
for x in student_scores:
  if x > Highest:
    Highest = x

print(f"The highest score in the class is: {Highest}")
##########################################################################

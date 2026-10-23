#Sample Data Script
#Assignment 1: Git and GitHub

students=[
{"name":"student 1",
"score":85},
{"name":"student 2",
"score":90},
{"name":"student 3",
"score":78},
{"name":"student 4",
"score":88}
 ]
 
print("Sample Student Data")
 
for student in students:
  print(student["name"],
"-", student["score"])

total=sum(student["score"]
for student in students)
average=total/len(students)

print("Average score:",
average)


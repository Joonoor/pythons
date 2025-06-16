from student import Student
from group import CourseGroup

student = Student("Dick", "Free", 17, "Loch")
classmate1 = Student("Mike", "Suck", 3, "Loch")
classmate2 = Student("Johnny", "Sins", 46, "Loch")

cours1 = CourseGroup(student, [classmate1, classmate2])

print(cours1)

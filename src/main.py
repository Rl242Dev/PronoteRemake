from classes.Grade import Grade
from classes.subject.SubjectType import SubjectType

grade = Grade(SubjectType.ENGLISH, 1, 15)

print(grade.grade)
print(grade.subject)
print(grade.coefficiant)
print(grade.title)
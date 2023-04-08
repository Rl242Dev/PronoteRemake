from classes.subject.SubjectType import SubjectType
from typing import Optional

class Grade:
    def __init__(self, subject: SubjectType, coefficiant: int, grade: int, title: Optional[str] = None) -> None:
        self.subject = subject
        self.coefficiant = coefficiant
        self.grade = grade
        self.title = title

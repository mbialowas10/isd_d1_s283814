"""This module defines the StudentDecorator class."""

from student.student import Student
from decimal import Decimal

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class StudentDecorator(Student):
    """Represents the decorator object of a student"""

    def __init__(self, student: Student) -> None:
        """Initializes a new instance of the StudentDecorator class
        
            Args:
                student (Student): The student to decorate
        """
        self.__student = student

    def get_grade_point_average(self) -> Decimal:
        """Returns the students grade point average
        
            Returns:
                Decimal: the student's GPA
        """
        return self.__student.get_grade_point_average()


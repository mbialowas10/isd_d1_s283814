"""This module defines the StudentCouncilDecorator class."""

from decimal import Decimal
from student.student import Student
from patterns.decorator.student_decorator import StudentDecorator

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class StudentCouncilDecorator(StudentDecorator):
    """ Represents the decorated object for the student"""

    def __init__(self, student: Student) -> None:
        """Initializes ta new instance of the StudentDecorator class
        
            Args: 
                student (Student) : The student to decorate
        """
        super().__init__(student)

    def get_grade_point_average(self) -> Decimal:
        """Returns the gpa for a student that in student council
        
            An increase to the gpa is based on the student's original gpa

            Returns: 
                Decimal: The gpa that a student obtains by joining student council
        """
        increases = {
            Decimal('4.13') : Decimal('.35'),
            Decimal('3.67') : Decimal('.19'),
            Decimal('2.40') : Decimal('.04')
        }
        increase = 0 

        for average in increases:
            if increase == 0 and super().get_grade_point_average() >= average:
                increase = increases[average]
                
        return min(super().get_grade_point_average() + increase, Decimal('4.5'))

"""This module defines the VolunteerDecorator class."""

from decimal import Decimal
from student.student import Student
from student.student_decorator import StudentDecorator

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class VolunteerDecorator(StudentDecorator):

    """Represent a decorator object for a student"""
    def __init__(self,student:Student)-> None:
        """Initializes a new instance of the Volunteer decorator class
        
            Args:
                student (Student): The student to decorate
                
        """
        super().__init__(student)

    def get_grade_point_average(self) -> Decimal:
        """Returns the GPS for a student who volunteers
        
            Returns:
                Decimal: The GPA of student who volunteers.
        """
        GRADE_POINT_AVERAGE_INCREASE = Decimal('.25')

        return min((super().get_point_grade_average() + GRADE_POINT_AVERAGE_INCREASE), Decimal('4.5'))

        




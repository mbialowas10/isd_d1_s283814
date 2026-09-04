"""This module defines the Course class."""

__author__ = "Michael Bialowas"
__version__ = "1.0.0"

from course.department import Department

class Course():
    """Represent a course at an education institution"""

    def __init__(self, 
                 name: str,
                 department: Department,
                 credit_hours: int):
        """Initializes a new instance of the Course class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is 
                delivered.
            credit_hours (int): The number of credit hours.
        
        Raises:
            ValueError: Raised when the name argument contains no
            non-whitespace characters or the credit_hours value is less 
            than or equal to zero.
        """

        if len(name.strip()) == 0:
            raise ValueError("name cannot be an empty string")

        if isinstance(credit_hours, int):
            if credit_hours <= 0:
                raise ValueError("credit hours must be a value greater than zero")
            else:
                self.__credit_hours = credit_hours

        self.__name = name.strip()
        self.__department = department
        # line 24 is redundant bc line 19 is already treating
        # self.__credit_hours = credit_hours
    @property
    def name(self) -> str:
        """Gets the name of the course.

        Returns:
            str: The name of the course.
        """
        return self.__name

    @property
    def department(self) -> Department:
        """Gets the department the course is delivered within.

        Returns:
            Department: The faculty department the course is managed from.
        """
        return self.__department

    @property
    def credit_hours(self) -> int:
         """Gets the number of credit hours for this course.

        Credit hours typically correlate with the number of instructional
        hours of a course.

        Returns:
            int: The number of credit hours for this course.
        """
        return self.__credit_hours

    @credit_hours.setter
    def credit_hours(self,credit_hours:int) ->None:
        """Sets the credit hours of the course.
        
        Args:
            credit_hours (int): The number of credit hours for this 
                course.

        Raises:
            ValueError: Raised when the credit_hours is not a value
                greater than zero.
        """
        if credit_hours <= 0:
            raise ValueError("credit hours must be a value greater than zero.")
        self.__credit_hours = credit_hours



    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
                representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """
        return (f"Course: {self.__name.title()}\n"
                f"Department: {self.__department.name.replace('_', ' ').title()} \n"
                f"Credit Hours: {self.__credit_hours}")
    

        
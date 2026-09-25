"""This module defines a LectureCourse Class"""

from course.course import Course
from course.department import Department
from course.student import Student

__author__ = "ACE Faculty <mbialowas@rrc.ca>"
__version__ = "1.0.0"

class LectureCourse(Course, object):
    """Represent a course that involves lectures"""

    def __init__(self,
                 name: str,
                 department: Department,
                 credit_hours: int,
                 lecture_hall: str) -> None:
        """Initialize a new instance of Course class
        
            Args:
                name (str): The name of the course
                department (Department) : The department name
                credit_hours (int) : the credit hours for course
                lecture_hall (str) : The location of the lecture.
            
                Raises:
                    ValueError: Raised when
                        - the name contains no non-whitespace characters
                        - the credit_hours is less than 0
                        - the lecture_hall is null
        """
        super().__init__(name,department, credit_hours)

        lecture_hall = lecture_hall.strip()

        if lecture_hall == "":
            raise ValueError("Lecture hall cannot be an empty string")

        self.__lecture_hall = lecture_hall

    @property
    def lecture_hall(self) -> str:
        """Gets the lecture hall that the course is delivered in

            Returns
                str: The lecture hall
        """
        return self.__lecture_hall

    def enroll_student(self, student: Student) -> None:
        """Enrolls a student in a course
        
            Args:
                student (Student) : The student to enroll in course
        """
        buffer = int(Course.ENROLLMENT_LIMIT * .1)
        if len(self.students) >= Course.ENROLLMENT_LIMIT + buffer:
            raise ValueError("Cannot enroll student; course at capacity")

        self.__students.append(student)

    def __str__(self) -> str:
        """ Returns the string representation of the object

            Returns:
                str: the string representation of the object
        """
        return (f"{super().str()}\n"
                f"Lecture Hall: {self.lecture_hall}")
        
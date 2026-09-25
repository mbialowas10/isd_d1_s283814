"""This module defines tests for the LectureCourse Class

    Example:
        $python -m unittest tests/test_course.py
"""

import unittest
from decimal import Decimal

from course.department import Department
from course.course import Course
from course.lecture_course import LectureCourse
from course.student import Student

__author__ = "Ace Faculty"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines the test for the __init__ method."""

    def test_lecture_hall_is_empty_string(self) -> None:
        """Tests for lecture hall attribute"""

        #Arrange/Act/Assert

        #Arrange/act
        with self.assertRaises(ValueError) as context:
            course = LectureCourse("ISD", 
                                   Department.COMPUTER_SCIENCE, 
                                   90,
                                   "")
            
            # assert
            self.assertEqual("", str(context.exception))

class TestEnrollStudent(unittest.TestCase):
    """Tests for enrolling a studnet"""

    def setUp(self) -> None:
        #arrange
        self.course = LectureCourse("ISD",
                                    Department.COMPUTER_SCIENCE,
                                    90,
                                    "A202")

    def test_enroll_student_at_capacity(self) -> None:
        # arrange
        # only allow students to enroll if within 10% cap
        capacity = Course.ENROLLMENT_LIMIT + int(Course.ENROLLMENT_LIMIT * 0.1)

        for _ in range(capacity):
            student = Student()
            self.course._Course__students.append(student)

        # act
        with self.assertRaises(ValueError) as context:
            student = Student()
            self.course.enroll_student(student)

        self.assertEqual("Cannot enroll student; course at capacity", 
                         str(context.exception))     
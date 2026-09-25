""""Unit tests for the Lab Course"""

import unittest
from course.lab_course import LabCourse
from course.course import  Course 
from course.department import Department
from course.student import Student

class TesLabCourse(unittest.TestCase):
    """Tests for the LabCourse class"""

    def setUp(self)-> None:
        self.course = LabCourse(
            "Chemistry",
            Department.MEDICINE,
            3
        )


    def test_init_new_instance(self)-> None:

        #Assert
        self.assertIsInstance(self.course, Course)
        self.assertEqual(self.course.name,"Chemistry")
        self.assertEqual(
            self.course.department,
            Department.MEDICINE
        )
        self.assertEqual(self.course.credit_hours, 3)
        self.assertEqual(
            self.course._LabCourse__lab_equipment,
            []
        )

    def test_enroll_student_at_capacity(self)-> None:
        # arrange
        capacity = Course.ENROLLMENT_LIMIT

        for _ in range(capacity):
            self.course.students.append(Student())

        student = Student()

        self.assertEqual(len(self.course.students),capacity)

        #act and assert
        with self.assertRaises(ValueError):
            self.course.enroll_student(student)

            
    
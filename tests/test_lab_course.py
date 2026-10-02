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


    def test_enroll_student_below_capacity(self) -> None:
        #arrange
        student = Student()

        #act
        self.course.enroll_student(student)

        # assert
        # list contains the student
        self.assertIn(student, self.course._Course__students)

        # list contains the correct number of students
        self.assertEqual(1, len(self.course._Course__students))

class TestAddLabEquipment(unittest.TestCase):
    """Defines tests for adding lab equipment"""

    def setUp(self) -> None:
        """setup that gets called first"""
        
        #arrange
        self.course = LabCourse("ISD", 
                                Department.COMPUTER_SCIENCE, 
                                90)


    def test_equipment_is_empty_string(self)-> None:
        # act
        with self.assertRaises(ValueError) as context:
            
            self.course.add_lab_equipment("")

        # assert
        self.assertEqual("equipment cannot be an empty string",
                         str(context.exception)) 


    def test_equipment_already_added(self) -> None:
        # revist this test... modifiy test next iteration
        # arrange
        lab_equipment = ["Microscope"]
        self.course._LabCourse__lab_equipment = lab_equipment

        # act
        self.course.add_lab_equipment("microscope")
        self.course.add_lab_equipment("microscope")

        # assert
        self.assertCountEqual(lab_equipment, self.course._LabCourse__lab_equipment)



    def test_equipment_is_updated(self) -> None:

        # arrange 
        lab_equipment="microscope"

        # act
        self.course.add_lab_equipment(lab_equipment)

        #assert
        self.assertIn(lab_equipment.title(), self.course._LabCourse__lab_equipment)
        self.assertEqual(1, len(self.course._LabCourse__lab_equipment))


class TestStr(unittest.TestCase, object):

    """ Defines test for the __str__ method"""        
    def setUp(self) -> None:
        # arrange
        self.course = LabCourse("isd", 
                                Department.COMPUTER_SCIENCE,
                                90)
        self.course._LabCourse__lab_equipment = ["Microscope"]

    def test_returns_string_representation(self) -> None:
        # act 
        actual = self.course.__str__()

        # assert
        expected = ("Course: Isd\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90\n"
                    "Lab Equipment: ['Microscope']")
        self.assertEqual(expected,actual)
import unittest
from course.department import Department

class TestDepartment(unittest.TestCase):
    """Define some tests for our enumeration values"""
    #Arrange, Act, Assert
    
    def test_enumeration_values_initialized(self):  
        #Assert
        self.assertEqual(1, Department.COMPUTER_SCIENCE.value)
        self.assertEqual(2, Department.EDUCATION.value)
        self.assertEqual(3, Department.ENGINEERING.value)
        self.assertEqual(4, Department.MEDICINE.value)


if __name__ == "__main__":
    unittest.main()

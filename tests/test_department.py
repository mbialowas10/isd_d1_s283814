"""This module defines tests for the Department enumeration."""

import unittest
from course.department import Department

__author__ = "Michael Bialowas <mbialowas@rrc.ca>"
__version__ = "1.0.0"

class TestDepartment(unittest.TestCase):
    """Represents departments within a post-secondary institution."""
    #Arrange, Act, Assert
    
    def test_enumeration_values_initialized(self):  
        #Assert
        self.assertEqual(1, Department.COMPUTER_SCIENCE.value)
        self.assertEqual(2, Department.EDUCATION.value)
        self.assertEqual(3, Department.ENGINEERING.value)
        self.assertEqual(4, Department.MEDICINE.value)


if __name__ == "__main__":
    unittest.main()

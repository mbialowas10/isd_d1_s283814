"""This module defines the StudentNumberGenerator aka Singleton pattern"""

__author__="ACE Faculty"
__version__="1.0.0"

class StudentNumberGenerator:
    """A singleton that generate student numbers"""

    __instance = None
    __next_student_number: int = 20_240_000

    def __new__(cls):
        """Return the single instance of the the Singleton class
        
            Returns:
                SingletonStudentManager: The single instance 
                of the SingletonStudentManager
        """
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @staticmethod
    def get_instance() -> StudentNumberGenerator:
        if not StudentNumberGenerator.__instance:
            StudentNumberGenerator.__instance = StudentNumberGenerator()
        return StudentNumberGenerator.__instance

    def get_next_student_number(self):
        """Returns the next available unique student number
        
            Returns:
                int: The next available student number
        """
        next_student_number = self.__next_student_number
        self.__next_student_number += 1
        return next_student_number
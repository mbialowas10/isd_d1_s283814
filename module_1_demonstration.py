"""This module is used to demonstrate concepts from module 1."""
from course.department import Department
from course.course import Course

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

def main():
    """The main entry point of the program."""
    try:
        course = Course("intermediate software development", Department.COMPUTER_SCIENCE,90)

        print(course)
    except AttributeError as error:
        print(error)

if __name__ == "__main__":
    main()

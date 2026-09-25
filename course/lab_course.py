""""The module defines the LabCourse"""

from course.course import Course
from course.department import Department
from course.student import Student

class LabCourse(Course):
    """Represent the lab Course"""

    def __init__(self, name: str, department: Department, credit_hours: int)-> None:
        """Initializes a new instance of the Course class
        
            Args:
                name (str): the name of the course
                department (Department): The department that offers the course
                credit_hours (int) : The number of credit hours
            
            Raises:
                ValueError: Raised
                - the name contains no non-whitespace characters
                - the credit hours value is less than or equal to. 
        """

        super().__init__(name,department, credit_hours)

        self.__lab_equipment = []

    def add_lab_equipment(self, equipment: str)-> None:

        """Add equipment to inventory list

            if equipment exists it won't be added

            Args:
                equipment(str) : The equipment for the course ie. Chemistry 

        """
        equipment = equipment.strip().title()

        if equipment == "":
            raise ValueError("equipment cannot be an empty string")

        if equipment not in self.__lab_equipment:
            self.__lab_equipment.append(equipment)

    def enroll_student(self, student:Student) -> None:
        """enrolls a student in a lab course
        
            Args:
                student: Student : The student being enrolled in course

            Raises:
                ValueError when:
                    - capacity reached
        """
        capacity = int(Course.ENROLLMENT_LIMIT/ 2)

        if len(self.students) >= capacity:
            raise ValueError("Cannot enroll student; course at capacity")
        self.students.append(student)

    def __str__(self) -> str:
        """Returns the Lab Course string representation
        
            Returns:
                str: The lab course string representation.
        """
        return (f"{super().__str__()}\n"
                f"Lab Equipment: {self.__lab_equipment}")
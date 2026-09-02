from course.department import Department

class Course():
    """Represent a course at an education institution"""

    def __init__(self, 
                 name: str,
                 department: Department,
                 credit_hours: int):
        """Initializes a new instance of Course class"""

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
        """Gets the name of the course
        
            Returns:
                str: The name of the course
        """
        return self.__name

    @property
    def department(self) -> int:
        return self.__department

    @property
    def credit_hours(self) -> int:
        return self.__credit_hours

    @credit_hours.setter
    def credit_hours(self,credit_hours:int) ->None:

        if credit_hours <= 0:
            raise ValueError("credit hours must be a value greater than zero.")
        self.__credit_hours = credit_hours



    def __str__(self) -> str:
        return (f"Course: {self.__name.title()}\n"
                f"Department: {self.__department.name.replace('_','').title()}\n"
                f"Credit Hours: {self.__credit_hours}")
    

        
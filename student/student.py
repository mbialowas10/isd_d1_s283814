from abc import ABC, abstractmethod
from decimal import Decimal

class Student(ABC):
    """This represents the student class."""

    @abstractmethod
    def get_grade_point_average(self) -> Decimal:
        """Returns the students grade point average (GPA)
        
            Returns:
                Decimal: The students GPA
        """
        pass
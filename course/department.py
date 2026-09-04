"""This module defines the Department enumeration.

Example:
    >>> print(Department.COMPUTER_SCIENCE)
    >>> Department.COMPUTER_SCIENCE
"""

from enum import Enum, auto

__author__ = "Michael Bialowas <mbialowas@rrc.ca>"
__version__ = "1.0.0"
class Department(Enum):
    """Represents departments within a post-secondary institution."""


    COMPUTER_SCIENCE = auto()
    """The computer science department."""

    EDUCATION = auto()
    """The education department."""

    ENGINEERING = auto()
    """The engineering department."""

    MEDICINE = auto()
    """The medicine department."""

    
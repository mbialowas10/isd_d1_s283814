"""Defines the StudentGradeDialog class."""
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QMessageBox
from decimal import Decimal


from student.college_student import CollegeStudent
from patterns.decorator.student_decorator import StudentDecorator
from student.volunteer_decorator import VolunteerDecorator
from student.student_council_decorator import StudentCouncilDecorator

from ui.base.grade_dialog import GradeDialog

__author__ = "ACE Faculty"
__version__ = "1.0.0"

class StudentGradeDialog(GradeDialog):
    """Represents a dialog window for updating a student's grade point
    average.
    """

    grade_updated = Signal(object)
    """Raise when the grade is update"""

    def accept(self) -> None:
        """Hide the modal dialog and sets the result code to expect"""
        self.grade_updated.emit(Decimal(self._grade_label.text()))
        return super().accept() # close window by calling parent class object 
    
    def __init__(self, student: CollegeStudent) -> None:
        """Initializes a new instance of the StudentGradeDialog class.
        
        Args:
            student (CollegeStudent): The student whose grade is being
                updated.
        """

        super().__init__()

        self.__student = student
        self.setWindowTitle(f"Grade Edit - {student.name}")
        self.__initialize_widgets()

    def __initialize_widgets(self):
        """Initialize the widgets on the window"""

        student = self.__student

        self._student_number_label.setText(str(student.student_number))
        self._student_name_label.setText(student.name)

        self._grade_label.setText("")
        self._update_button.setEnabled(False)

        for combobox in self._grade_comboboxes:
            combobox.setCurrentIndex(-1)

        for line_edit in self._credit_hour_line_edits:
            line_edit.setText("")

        for combobox in self._grade_comboboxes:
            combobox.currentIndexChanged.connect(self.__on_input_changed)

        for line_edit in self._credit_hour_line_edits:
            line_edit.textChanged.connect(self.__on_input_changed)

        # todo - decorators
        self._volunteer_checkbox.checkStateChanged.connect(self.__on_input_changed)
        self._student_council_checkbox.checkStateChanged.connect(self.__on_input_changed)

        self._update_button.clicked.connect(self.__on_update_button_clicked)


    @Slot()
    def __on_update_button_clicked(self) -> None:
        """Hannles the clicked event on the update action"""
        message_box = QMessageBox()
        message_box.setWindowTitle("Update Grade")
        message_box.setText("Do you wish to update the student's grade?")
        message_box.setIcon(QMessageBox.Icon.Question)

        message_box.setStandardButtons(QMessageBox.StandardButton.Yes |
                                       QMessageBox.StandardButton.No |
                                       QMessageBox.StandardButton.Cancel)
        
        message_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        answer = message_box.exec()

        if answer == QMessageBox.StandardButton.No:
            self.reject()
        elif answer == QMessageBox.StandardButton.Yes:
            self.accept()

    

    @Slot()
    def __on_input_changed(self) -> None:
        """Handles the changed events of the input widgets in this window"""
        
        total_quality_points = Decimal(0)
        total_credit_hours = 0 

        for combobox, line_edit in \
        zip(self._grade_comboboxes, self._credit_hour_line_edits):
            if combobox.currentIndex() == -1 or \
                line_edit.text() == "":
                self._grade_label.setText("Nil")
                return

            credit_hours = int(line_edit.text()) # value of credits
            total_quality_points += \
                self.GRADES[combobox.currentText()] * credit_hours

            total_credit_hours += credit_hours

        grade_point_average = round( total_quality_points / total_credit_hours, 1)

        # tempory Object
        student = CollegeStudent(self.__student.name, grade_point_average)

        if self._volunteer_checkbox.isChecked():
            student = VolunteerDecorator(student)

        if self._student_council_checkbox.isChecked():
            student = StudentCouncilDecorator(student)

        self._grade_label.setText(str(student.get_grade_point_average()))

        self._update_button.setEnabled(True)







        

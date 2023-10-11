import datetime as dt
from PySide6.QtWidgets import QWidget, QMessageBox
from ui_addtask import Ui_add_task


class AddTaskWidget(QWidget, Ui_add_task):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model
        # connect button signals to slots
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

    def is_valid(self, task, date):  # validation on user inputs
        today = dt.date.today()
        if task.isspace() or task == '':
            QMessageBox.warning(self, 'To-Do List', 'You have no task?\n\nPlease enter a task.')
            return False
        elif date < today:
            QMessageBox.warning(self, 'To-Do List', 'Woah! Are you a time traveler?\n\n'
                                                    'Please enter a date from today onwards.')
            return False
        elif (task.isspace() or task == '') and date < today:
            QMessageBox.warning(self, 'To-Do List', 'Woah! Are you a time traveler with no task?\n\n'
                                                    'Please enter a task and a date from today onwards.')
            return False
        return True

    def ok(self):  # adds user input into database
        selected_date = self.due_date_widget.selectedDate()
        year = selected_date.year()
        month = selected_date.month()
        day = selected_date.day()
        is_valid = self.is_valid(self.task_line_edit.text(), dt.date(year, month, day))
        if is_valid:
            task = self.task_line_edit.text()
            due_date = dt.date(year, month, day)
            date_converted = dt.date.fromisoformat(str(due_date))
            formatted_date = date_converted.strftime("%b %d %Y")
            priority = self.priority_combobox.currentText()
            is_complete = 'No'
            record = self.model.record()
            record.setValue('task', task)
            record.setValue('due_date', formatted_date)
            record.setValue('priority', priority)
            record.setValue('is_complete', is_complete)
            self.model.insertRecord(-1, record)
            self.model.select()
            self.close()

    def cancel(self):
        self.close()

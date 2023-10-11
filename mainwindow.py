from PySide6.QtCore import Qt, QEventLoop
from PySide6.QtWidgets import QMainWindow, QMessageBox, QMenu
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from ui_mainwindow import Ui_MainWindow
from addtask import AddTaskWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.add_task_widget = None
        # connect and open database
        # creates database if none exists
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("To_Do_List.db")
        self.db.open()
        # cursor
        self.query = QSqlQuery()
        # create database table if none exists
        self.create_db_table()
        # loads database into a tablemodel
        self.model = QSqlTableModel(self, self.db)
        # connect action signals to slots
        self.actionQuit.triggered.connect(self.quit)
        self.actionAddTask.triggered.connect(self.add)
        self.actionDeleteTask.triggered.connect(self.delete)
        self.actionMarkTaskComplete.triggered.connect(self.mark_complete)
        self.actionAbout.triggered.connect(self.about)
        # displays to-do list on app start up
        self.display_todo_list()
        # connect context menu signal and slot
        self.task_table.customContextMenuRequested.connect(self.show_context_menu)
        # initialize QMenu for context menu
        self.task_table_context_meu = QMenu()

    def quit(self):  # closes database and quits the app
        self.db.close()
        self.app.quit()

    def create_db_table(self):  # creates table if none exists
        self.query.exec("CREATE TABLE IF NOT EXISTS todolist("
                        "task_id INTEGER PRIMARY KEY, task, due_date, priority, is_complete)")

    def add(self):  # opens a new window to add a task
        self.add_task_widget = AddTaskWidget(self.model)
        self.add_task_widget.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.add_task_widget.show()
        loop = QEventLoop()
        self.add_task_widget.destroyed.connect(loop.quit())
        loop.exec()

    def delete(self):  # deletes selected task from tableview
        try:
            selected = self.task_table.selectedIndexes()
            rows = set(index.row() for index in selected)
            rows = list(rows)
            rows.sort()
            first = rows[0]
            self.model.removeRow(first)
            self.model.select()
        except IndexError:
            QMessageBox.warning(self, 'To-Do List', 'Please select a task to delete.')

    def mark_complete(self):  # marks a task complete
        try:
            selected = self.task_table.selectedIndexes()
            rows = set(index.row() for index in selected)
            columns = set(index.column() for index in selected)
            rows = list(rows)
            columns = list(columns)
            self.model.setData(self.model.index(rows[0], columns[4]), 'Yes')
            self.model.submitAll()
        except IndexError:
            QMessageBox.warning(self, 'To-Do List', 'Please select a task to mark complete.')

    def show_context_menu(self, pos):  # context menu for added functionality
        self.task_table_context_meu.addAction(self.actionAddTask)
        self.task_table_context_meu.addAction(self.actionDeleteTask)
        self.task_table_context_meu.addAction(self.actionMarkTaskComplete)
        self.task_table_context_meu.popup(self.task_table.viewport().mapToGlobal(pos))

    def about(self):
        QMessageBox.information(self, 'To-Do List', 'A simple to-do list app written in Python using various modules '
                                                    'in PySide6.')

    def keyPressEvent(self, event):  # shortcuts for actions (overrides module method)
        key = event.key()
        modifier = event.modifiers()
        if modifier and Qt.Key.Key_Alt:
            if key == Qt.Key.Key_A:
                self.add()
            elif key == Qt.Key.Key_D:
                self.delete()
            elif key == Qt.Key.Key_X:
                self.mark_complete()
            elif key == Qt.Key.Key_Q:
                self.quit()
        super(MainWindow, self).keyPressEvent(event)

    def display_todo_list(self):  # displays database table into tableview
        self.model.setTable('todolist')
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, '#')
        self.model.setHeaderData(1, Qt.Horizontal, 'Task')
        self.model.setHeaderData(2, Qt.Horizontal, 'Due Date')
        self.model.setHeaderData(3, Qt.Horizontal, 'Priority')
        self.model.setHeaderData(4, Qt.Horizontal, 'Complete')
        self.task_table.setModel(self.model)
        self.task_table.setColumnWidth(0, 45)  # task id
        self.task_table.setColumnWidth(1, 330)  # task
        self.task_table.setColumnWidth(2, 110)  # due date
        self.task_table.setColumnWidth(3, 80)  # priority
        self.task_table.setColumnWidth(4, 80)  # complete

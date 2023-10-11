# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addtask.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_add_task(object):
    def setupUi(self, add_task):
        if not add_task.objectName():
            add_task.setObjectName(u"add_task")
        add_task.setWindowModality(Qt.ApplicationModal)
        add_task.resize(341, 331)
        add_task.setMinimumSize(QSize(341, 331))
        add_task.setMaximumSize(QSize(341, 331))
        add_task.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/images/checklist.png", QSize(), QIcon.Normal, QIcon.Off)
        add_task.setWindowIcon(icon)
        self.layoutWidget = QWidget(add_task)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 321, 311))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.task_line_edit = QLineEdit(self.layoutWidget)
        self.task_line_edit.setObjectName(u"task_line_edit")
        self.task_line_edit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.task_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.priority_combobox = QComboBox(self.layoutWidget)
        self.priority_combobox.addItem("")
        self.priority_combobox.addItem("")
        self.priority_combobox.addItem("")
        self.priority_combobox.setObjectName(u"priority_combobox")

        self.horizontalLayout_2.addWidget(self.priority_combobox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.due_date_widget = QCalendarWidget(self.layoutWidget)
        self.due_date_widget.setObjectName(u"due_date_widget")
        self.due_date_widget.setContextMenuPolicy(Qt.NoContextMenu)
        self.due_date_widget.setGridVisible(False)
        self.due_date_widget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.due_date_widget.setNavigationBarVisible(True)
        self.due_date_widget.setDateEditEnabled(True)

        self.verticalLayout.addWidget(self.due_date_widget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ok_button = QPushButton(self.layoutWidget)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_3.addWidget(self.ok_button)

        self.cancel_button = QPushButton(self.layoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(add_task)

        QMetaObject.connectSlotsByName(add_task)
    # setupUi

    def retranslateUi(self, add_task):
        add_task.setWindowTitle(QCoreApplication.translate("add_task", u"Add Task", None))
        self.label.setText(QCoreApplication.translate("add_task", u"Task:", None))
        self.label_3.setText(QCoreApplication.translate("add_task", u"Priority:", None))
        self.priority_combobox.setItemText(0, QCoreApplication.translate("add_task", u"High", None))
        self.priority_combobox.setItemText(1, QCoreApplication.translate("add_task", u"Medium", None))
        self.priority_combobox.setItemText(2, QCoreApplication.translate("add_task", u"Low", None))

        self.label_2.setText(QCoreApplication.translate("add_task", u"Due Date:", None))
        self.ok_button.setText(QCoreApplication.translate("add_task", u"Ok", None))
        self.cancel_button.setText(QCoreApplication.translate("add_task", u"Cancel", None))
    # retranslateUi


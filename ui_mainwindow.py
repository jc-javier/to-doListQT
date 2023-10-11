# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableView, QToolBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(668, 487)
        MainWindow.setMinimumSize(QSize(668, 487))
        MainWindow.setMaximumSize(QSize(668, 487))
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u":/images/checklist.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAddTask = QAction(MainWindow)
        self.actionAddTask.setObjectName(u"actionAddTask")
        icon1 = QIcon()
        icon1.addFile(u":/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddTask.setIcon(icon1)
        self.actionDeleteTask = QAction(MainWindow)
        self.actionDeleteTask.setObjectName(u"actionDeleteTask")
        icon2 = QIcon()
        icon2.addFile(u":/images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDeleteTask.setIcon(icon2)
        self.actionMarkTaskComplete = QAction(MainWindow)
        self.actionMarkTaskComplete.setObjectName(u"actionMarkTaskComplete")
        icon3 = QIcon()
        icon3.addFile(u":/images/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMarkTaskComplete.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.task_table = QTableView(self.centralwidget)
        self.task_table.setObjectName(u"task_table")
        self.task_table.setMinimumSize(QSize(650, 400))
        self.task_table.setMaximumSize(QSize(650, 400))
        self.task_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.task_table.setAcceptDrops(False)
        self.task_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.task_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.task_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.task_table.setSortingEnabled(False)
        self.task_table.horizontalHeader().setHighlightSections(False)
        self.task_table.verticalHeader().setVisible(False)
        self.task_table.verticalHeader().setDefaultSectionSize(24)

        self.verticalLayout.addWidget(self.task_table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 668, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QSize(668, 26))
        self.toolBar.setMaximumSize(QSize(668, 26))
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.TopToolBarArea)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionAddTask)
        self.menuEdit.addAction(self.actionDeleteTask)
        self.menuEdit.addAction(self.actionMarkTaskComplete)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionAddTask)
        self.toolBar.addAction(self.actionDeleteTask)
        self.toolBar.addAction(self.actionMarkTaskComplete)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To-Do List", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("MainWindow", u"Alt+Q", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddTask.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.actionAddTask.setToolTip(QCoreApplication.translate("MainWindow", u"Alt+A", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAddTask.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionDeleteTask.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.actionDeleteTask.setToolTip(QCoreApplication.translate("MainWindow", u"Alt+D", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionDeleteTask.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionMarkTaskComplete.setText(QCoreApplication.translate("MainWindow", u"Mark Complete", None))
#if QT_CONFIG(tooltip)
        self.actionMarkTaskComplete.setToolTip(QCoreApplication.translate("MainWindow", u"Alt+X", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionMarkTaskComplete.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\Notery\Admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 582)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 951, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralWidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_add_book = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rsc/rsc/manage_ebooks_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_book.setIcon(icon)
        self.action_add_book.setObjectName("action_add_book")
        self.action_manage_students = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/rsc/rsc/manage_students_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_manage_students.setIcon(icon1)
        self.action_manage_students.setObjectName("action_manage_students")
        self.action_report = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/rsc/rsc/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_report.setIcon(icon2)
        self.action_report.setObjectName("action_report")
        self.action_delete = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/rsc/rsc/trash_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete.setIcon(icon3)
        self.action_delete.setObjectName("action_delete")
        self.action_star = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/rsc/rsc/star_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_star.setIcon(icon4)
        self.action_star.setObjectName("action_star")
        self.action_settings = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/rsc/rsc/settings_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_settings.setIcon(icon5)
        self.action_settings.setObjectName("action_settings")
        self.action_add_record = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/rsc/rsc/add_record_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_record.setIcon(icon6)
        self.action_add_record.setObjectName("action_add_record")
        self.action_edit_record = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/rsc/rsc/edit_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_record.setIcon(icon7)
        self.action_edit_record.setObjectName("action_edit_record")
        self.toolBar.addAction(self.action_add_record)
        self.toolBar.addAction(self.action_edit_record)
        self.toolBar.addAction(self.action_star)
        self.toolBar.addAction(self.action_add_book)
        self.toolBar.addAction(self.action_manage_students)
        self.toolBar.addAction(self.action_report)
        self.toolBar.addAction(self.action_settings)
        self.toolBar.addAction(self.action_delete)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_add_book.setText(_translate("MainWindow", "Add Book"))
        self.action_manage_students.setText(_translate("MainWindow", "Manage Students"))
        self.action_report.setText(_translate("MainWindow", "Report"))
        self.action_delete.setText(_translate("MainWindow", "Delete"))
        self.action_star.setText(_translate("MainWindow", "Star"))
        self.action_settings.setText(_translate("MainWindow", "Settings"))
        self.action_add_record.setText(_translate("MainWindow", "Add Record"))
        self.action_edit_record.setText(_translate("MainWindow", "Edit Record"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


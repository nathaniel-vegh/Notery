# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\Notery\Student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BookStorage import BookStorageViewer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 580)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.storageView = BookStorageViewer()
        self.verticalLayout.addWidget(self.storageView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(70, 70))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_settings = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rsc/rsc/settings_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_settings.setIcon(icon)
        self.action_settings.setObjectName("action_settings")
        self.actionBorrow = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/rsc/rsc/borrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBorrow.setIcon(icon1)
        self.actionBorrow.setObjectName("actionBorrow")
        self.actionReturn = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/rsc/rsc/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReturn.setIcon(icon2)
        self.actionReturn.setObjectName("actionReturn")
        self.action_report = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/rsc/rsc/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_report.setIcon(icon3)
        self.action_report.setObjectName("action_report")
        self.action_star = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/rsc/rsc/star_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_star.setIcon(icon4)
        self.action_star.setObjectName("action_star")
        self.toolBar.addAction(self.actionBorrow)
        self.toolBar.addAction(self.actionReturn)
        self.toolBar.addAction(self.action_star)
        self.toolBar.addAction(self.action_report)
        self.toolBar.addAction(self.action_settings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notery"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_settings.setText(_translate("MainWindow", "Settings"))
        self.actionBorrow.setText(_translate("MainWindow", "Borrow"))
        self.actionReturn.setText(_translate("MainWindow", "Return"))
        self.action_report.setText(_translate("MainWindow", "Report"))
        self.action_star.setText(_translate("MainWindow", "Star"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


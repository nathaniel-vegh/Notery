# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\Notery\Student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BookStorage import BookStorageViewer

class Ui_self(object):
    def setupUi(self, self):
        self.setObjectName("self")
        self.resize(950, 580)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.storageView = BookStorageViewer()
        self.verticalLayout.addWidget(self.storageView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralWidget)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setIconSize(QtCore.QSize(70, 70))
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_settings = QtWidgets.QAction(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rsc/rsc/settings_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_settings.setIcon(icon)
        self.action_settings.setObjectName("action_settings")
        self.actionBorrow = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/rsc/rsc/borrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBorrow.setIcon(icon1)
        self.actionBorrow.setObjectName("actionBorrow")
        self.actionReturn = QtWidgets.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/rsc/rsc/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReturn.setIcon(icon2)
        self.actionReturn.setObjectName("actionReturn")
        self.action_report = QtWidgets.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/rsc/rsc/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_report.setIcon(icon3)
        self.action_report.setObjectName("action_report")
        self.action_star = QtWidgets.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/rsc/rsc/star_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_star.setIcon(icon4)
        self.action_star.setObjectName("action_star")
        self.toolBar.addAction(self.actionBorrow)
        self.toolBar.addAction(self.actionReturn)
        self.toolBar.addAction(self.action_star)
        self.toolBar.addAction(self.action_report)
        self.toolBar.addAction(self.action_settings)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Notery"))
        self.toolBar.setWindowTitle(_translate("self", "toolBar"))
        self.action_settings.setText(_translate("self", "Settings"))
        self.actionBorrow.setText(_translate("self", "Borrow"))
        self.actionReturn.setText(_translate("self", "Return"))
        self.action_report.setText(_translate("self", "Report"))
        self.action_star.setText(_translate("self", "Star"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.Qself()
    ui = Ui_self()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())


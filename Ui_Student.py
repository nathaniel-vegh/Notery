# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\Notery\Student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sip
from bookStorage import BookStorageViewer
from borrowBookDialog import borrowBookDialog
from returnBookDialog import returnBookDialog
from borrowStatus import BorrowStatusViewer


class Ui_Student(QMainWindow):
    def __init__(self,  studentId):
        super().__init__()
        self.studentId = studentId
        self.resize(950,  580)
        self.setWindowTitle("Notery")
        self.setupUi()
        
    def setupUi(self):
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
        self.action_status = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/rsc/rsc/studying.png"), QtGui.QIcon.Normal,  QtGui.QIcon.Off)
        self.action_status.setIcon(icon5)
        self.action_status.setObjectName("action_status")
        self.action_allBooks = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/rsc/rsc/manage_ebooks_button.png"), QtGui.QIcon.Normal,  QtGui.QIcon.Off)
        self.action_status.setIcon(icon6)
        self.action_status.setObjectName("action_all_books")

        self.toolBar.addAction(self.actionBorrow)
        self.toolBar.addAction(self.actionReturn)
        self.toolBar.addAction(self.action_star)
        self.toolBar.addAction(self.action_report)
        self.toolBar.addAction(self.action_settings)
        self.toolBar.addAction(self.action_status)
        self.toolBar.addAction(self.action_allBooks)
        self.toolBar.actionTriggered[QAction].connect(self.toolBarTriggered)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Notery"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_settings.setText(_translate("MainWindow", "Settings"))
        self.actionBorrow.setText(_translate("MainWindow", "Borrow"))
        self.actionReturn.setText(_translate("MainWindow", "Return"))
        self.action_report.setText(_translate("MainWindow", "Report"))
        self.action_star.setText(_translate("MainWindow", "Star"))
        self.action_status.setText(_translate("MainWindow", "Check Status"))
        self.action_allBooks.setText(_translate("MainWindow", "All Books"))

    def borrowBookClicked(self):
        borrowDialog = borrowBookDialog(self.studentId,  self)
        borrowDialog.borrow_book_successful_signal.connect(BorrowStatusViewer.borrowedQuery)
        borrowDialog.borrow_book_successful_signal.connect(self.storageView.searchButtonClicked)
        borrowDialog.show()
        borrowDialog.exec_()
        return
        
    def returnBookClicked(self):
        returnDialog = returnBookDialog(self.studentId,  self)
        returnDialog.return_book_successful_signal.connect(BorrowStatusViewer.returnedQuery)
        returnDialog.return_book_successful_signal.connect(BorrowStatusViewer.borrowedQuery)
        returnDialog.return_book_successful_signal.connect(self.storageView.searchButtonClicked)
        returnDialog.show()
        returnDialog.exec_()
        
    def allBookButtonClicked(self):
        self.gridLayout.removeWidget(self.borrowStatusView)
        sip.delete(self.borrowStatusView)
        self.borrowStatusView = BorrowStatusViewer(self.studentId)
        self.storageView = BookStorageViewer()
        self.gridLayout.addWidget(self.storageView)
        self.action_allBooks.setEnabled(False)
        self.action_status.setEnabled(True)
        return
        
    def myBookStatusClicked(self):
        self.gridLayout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = BookStorageViewer()
        self.borrowStatusView = BorrowStatusViewer(self.studentId)
        self.gridLayout.addWidget(self.borrowStatusView)
        self.action_allBooks.setEnabled(True)
        self.action_status.setEnabled(False)        
        return
        
    def toolBarTriggered(self,  a):
        if(a.text() == "Borrow"):
            self.borrowBookClicked()
        if(a.text() == "Return"):
            self.returnBookClicked()
        if(a.text() == "Check Status"):
            self.myBookStatusClicked()
        if(a.text() == "All Books"):
            self.allBookButtonClicked()
        
import resources_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./rsc/ereader.png"))
    mainWindow = Ui_Student("0000000001")
    mainWindow.show()
    sys.exit(app.exec_())

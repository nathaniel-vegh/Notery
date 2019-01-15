# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\E-Book2\SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import hashlib
from PyQt5.QtSql import *

class Ui_Dialog(QWidget):
    is_admin_signal =  pyqtSignal()
    is_student_signal = pyqtSignal(str)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(486, 309)
        #Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        Dialog.setSizeGripEnabled(True)
        self.SignUpButton = QtWidgets.QPushButton(Dialog)
        self.SignUpButton.setGeometry(QtCore.QRect(426, 5, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(11)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("color:rgb(32, 208, 194)")
        self.SignUpButton.setFlat(True)
        self.SignUpButton.setObjectName("SignUpButton")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 33, 491, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(13, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(14, 120, 134)\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(273, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:rgb(14, 120, 134)")
        self.label_15.setObjectName("label_15")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(172, 52, 128, 128))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-image:url(:/rsc/rsc/studying.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(140, 190, 191, 48))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.IdLineEdit = QtWidgets.QLineEdit(self.widget)
        self.IdLineEdit.setToolTip("")
        self.IdLineEdit.setStatusTip("")
        self.IdLineEdit.setText("")
        self.IdLineEdit.setObjectName("IdLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.IdLineEdit)
        self.SignInPasswordLineEdit = QtWidgets.QLineEdit(self.widget)
        self.SignInPasswordLineEdit.setObjectName("SignInPasswordLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SignInPasswordLineEdit)
        self.SignInButton = QtWidgets.QPushButton(Dialog)
        self.SignInButton.setGeometry(QtCore.QRect(164, 250, 152, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignInButton.sizePolicy().hasHeightForWidth())
        self.SignInButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SignInButton.setFont(font)
        self.SignInButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SignInButton.setStyleSheet("background-color:rgb(32, 208, 194);\n"
"color:white;")
        self.SignInButton.setAutoDefault(True)
        self.SignInButton.setDefault(False)
        self.SignInButton.setFlat(False)
        self.SignInButton.setObjectName("SignInButton")

        self.SignInButton.clicked.connect(self.SignInCheck)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SignUpButton.setText(_translate("Dialog", "Sign up"))
        self.label_2.setText(_translate("Dialog", "Notery"))
        self.label_15.setText(_translate("Dialog", "Don\'t have an account?"))
        self.IdLineEdit.setPlaceholderText(_translate("Dialog", "Id"))
        self.SignInPasswordLineEdit.setPlaceholderText(_translate("Dialog", "Password"))
        self.SignInButton.setText(_translate("Dialog", "Sign In"))

    def SignInCheck(self):
        studentId = self.IdLineEdit.text()
        password = self.SignInPasswordLineEdit.text()
        if (studentId == "" or password == ""):
            print(QMessageBox.warning(self,  "Warning",  "User name and password cannot be empty", QMessageBox.Ok))
            return
        # databse
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/FBLAE-Book2dbebook.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM User WHERE StudentId='%s'"%(studentId)
        query.exec_(sql)
        db.close()
        
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        if (not query.next()):
            print(QMessageBox.information(self,  "Information",  "The account does not exist",  QMessageBox.Ok))
        else:
            if(studentId == query.value(0) and hl.hexdigest() == query.value(2)):
                # If is admin
                if (query.value(3)==1):
                    self.is_admin_signal.emit()
                else:
                    self.is_student_signal.emit(studentId)
            else:
                print(QMessageBox.information(self,  "Information",  "Password incorrect",  QMessageBox.Ok))
        return
        
        

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


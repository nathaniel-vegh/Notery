# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FBLA\E-Book2\SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(486, 309)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
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
        self.CreateAccountButton_2 = QtWidgets.QPushButton(Dialog)
        self.CreateAccountButton_2.setGeometry(QtCore.QRect(164, 250, 152, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateAccountButton_2.sizePolicy().hasHeightForWidth())
        self.CreateAccountButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountButton_2.setFont(font)
        self.CreateAccountButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CreateAccountButton_2.setStyleSheet("background-color:rgb(32, 208, 194);\n"
"color:white;")
        self.CreateAccountButton_2.setAutoDefault(True)
        self.CreateAccountButton_2.setDefault(False)
        self.CreateAccountButton_2.setFlat(False)
        self.CreateAccountButton_2.setObjectName("CreateAccountButton_2")

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
        self.CreateAccountButton_2.setText(_translate("Dialog", "Sign In"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


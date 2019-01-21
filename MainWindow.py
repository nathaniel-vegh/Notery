import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from Ui_SignIn import Ui_SignIn
from Ui_SignUp import Ui_SignUp
import sip
from Ui_Admin import Ui_Admin
from Ui_Student import Ui_Student


class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        super(MainWindow, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.widget = Ui_SignIn()
        self.resize(486, 320)
        self.setWindowTitle("Notery")
        self.setCentralWidget(self.widget)
        bar = self.menuBar()
        self.Menu = bar.addMenu("Menu")
        self.signUpAction = QAction("Register", self)
        self.signInAction = QAction("Sign In", self)
        self.quitSignInAction = QAction("Sign Out", self)
        self.quitAction = QAction("Exit", self)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(False)
        self.widget.is_admin_signal.connect(self.adminSignIn)
        self.widget.is_student_signal[str].connect(self.studentSignIn)
        self.Menu.triggered[QAction].connect(self.menuTriggered)

    def adminSignIn(self):
        sip.delete(self.widget)
        self.resize(950, 580)
        self.widget = Ui_Admin()
        self.setCentralWidget(self.widget)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def studentSignIn(self, studentId):
        sip.delete(self.widget)
        self.resize(950,  580)
        self.widget = Ui_Student(studentId)
        self.setCentralWidget(self.widget)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        if (q.text() == "Register"):
            sip.delete(self.widget)
            self.widget = Ui_SignUp()
            self.setCentralWidget(self.widget)
            self.widget.student_sign_up_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(False)
            self.signInAction.setEnabled(True)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "Sign Out"):
            sip.delete(self.widget)
            self.resize(486,  309)
            self.widget = Ui_SignIn()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "Sign In"):
            sip.delete(self.widget)
            self.widget = Ui_SignIn()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "Exit"):
            qApp = QApplication.instance()
            qApp.quit()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./rsc/ereader.png"))
    mainMindow = MainWindow()
    mainMindow.show()
    sys.exit(app.exec_())

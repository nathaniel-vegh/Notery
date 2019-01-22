import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import time


class returnBookDialog(QDialog):
    return_book_successful_signal=pyqtSignal()

    def __init__(self, StudentId,  parent=None):
        super(returnBookDialog, self).__init__(parent)
        self.studentId = StudentId
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Return Book")

    def setUpUI(self):
        BookCategory = ["Technology", "Social Science", "Politics", "Law", "Military", "Economics", "Culture", "Education", "Physical Education", "Language Arts", "Arts", "History"
            , "Geography", "Astronomy", "Biology", "Medicine", "Philosophy"]
        self.resize(300, 250)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.borrowStudentLabel = QLabel("Borrower:")
        self.borrowStudentIdLabel = QLabel(self.studentId)
        self.bookNameLabel = QLabel("Book Name:")
        self.bookIdLabel = QLabel("Book Code:")
        self.authNameLabel = QLabel("Author:")
        self.categoryLabel = QLabel("Category:")
        self.publisherLabel = QLabel("Publisher:")
        self.publishDateLabel = QLabel("Publish Date:")

        self.returnBookButton = QPushButton("Return")

        self.bookNameEdit = QLineEdit()
        self.bookIdEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.addItems(BookCategory)
        self.publisherEdit = QLineEdit()
        self.publishTime = QLineEdit()
        # self.publishDateEdit = QLineEdit()

        self.bookNameEdit.setMaxLength(10)
        self.bookIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)

        self.layout.addRow(self.borrowStudentLabel,  self.borrowStudentIdLabel)
        self.layout.addRow(self.bookNameLabel, self.bookNameEdit)
        self.layout.addRow(self.bookIdLabel, self.bookIdEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow(self.returnBookButton)

        font = QFont()
        font.setFamily("Candara")
        font.setPixelSize(20)
        font.setPixelSize(14)
        self.borrowStudentIdLabel.setFont(font)
        self.borrowStudentLabel.setFont(font)
        self.bookNameLabel.setFont(font)
        self.bookIdLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)

        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setReadOnly(True)
        self.bookNameEdit.setStyleSheet("background-color:#dddddd")
        self.bookIdEdit.setFont(font)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setReadOnly(True)
        self.authNameEdit.setStyleSheet("background-color:#dddddd")
        self.publisherEdit.setFont(font)
        self.publisherEdit.setReadOnly(True)
        self.publisherEdit.setStyleSheet("background-color:#dddddd")
        self.publishTime.setFont(font)
        self.publishTime.setStyleSheet("background-color:#dddddd")
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setStyleSheet("background-color:#dddddd")

        font.setPixelSize(16)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setFixedHeight(32)
        self.returnBookButton.setFixedWidth(280)
        self.returnBookButton.setStyleSheet("background-color:rgb(255, 117, 124);\n"
"color:white;")
        self.layout.setVerticalSpacing(10)
        
        self.returnBookButton.clicked.connect(self.returnButtonClicked)
        self.bookIdEdit.textChanged.connect(self.bookIdEditChanged)
        
    def returnButtonClicked(self):
        BookId = self.bookIdEdit.text()
        if (BookId == ""):
            print(QMessageBox.warning(self, "Warning", "The book you are returning is not in our system", QMessageBox.Yes, QMessageBox.Yes))
            return
        db = db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/FBLAE-Book2dbebook.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" %(self.studentId,BookId)
        query.exec_(sql)
        if (not query.next()):
            print(QMessageBox.information(self, "Information", "You have not borrowed this book", QMessageBox.Yes, QMessageBox.Yes))
            return
        sql = "UPDATE User SET NumBorrowed=NumBorrowed-1 WHERE StudentId='%s'" % self.studentId
        query.exec_(sql)
        db.commit()
        sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow+1 WHERE BookId='%s'" % BookId
        query.exec_(sql)
        db.commit()
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (timenow,self.studentId,BookId)
        query.exec_(sql)
        db.commit()
        print(QMessageBox.information(self, "Information", "Book returned", QMessageBox.Yes, QMessageBox.Yes))
        self.return_book_successful_signal.emit()
        self.close()
        return

    def bookIdEditChanged(self):
        bookId = self.bookIdEdit.text()
        if (bookId == ""):
            self.bookNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.publishTime.clear()
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/FBLAE-Book2dbebook.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.studentId, bookId)
        query.exec_(sql)
        if (query.next()):
            sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
            query.exec_(sql)
            if (query.next()):
                self.bookNameEdit.setText(query.value(0))
                self.authNameEdit.setText(query.value(2))
                self.categoryComboBox.setCurrentText(query.value(3))
                self.publisherEdit.setText(query.value(4))
                self.publishTime.setText(query.value(5))
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./rsc/manage_ebooks_button.png"))
    mainMindow = returnBookDialog("0000000001")
    mainMindow.show()
    sys.exit(app.exec_())

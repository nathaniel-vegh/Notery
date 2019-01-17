import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
from PyQt5.QtSql import *


class addBookDialog(QDialog):
    add_book_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addBookDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Add Book")

    def setUpUI(self):

        BookCategory = ["Technology", "Social Science", "Politics", "Law", "Military", "Economics", "Culture", "Education", "Physical Education", "Language Arts", "Arts", "History"
            , "Geography", "Astronomy", "Biology", "Medicine", "Philosophy"]
        self.resize(300, 285)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        #self.titlelabel = QLabel("Add Book")
        self.bookNameLabel = QLabel("Book Name:")
        self.bookIdLabel = QLabel("Book Code:")
        self.authNameLabel = QLabel("Author:")
        self.categoryLabel = QLabel("Category:")
        self.publisherLabel = QLabel("Publisher:")
        self.publishDateLabel = QLabel("Publish Date:")
        self.addNumLabel = QLabel("Storage:")
        self.addBookButton = QPushButton("Add Book")
        self.bookNameEdit = QLineEdit()
        self.bookIdEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.addItems(BookCategory)
        self.publisherEdit = QLineEdit()
        self.publishTime = QDateTimeEdit()
        self.publishTime.setDisplayFormat("yyyy-MM-dd")
        self.addNumEdit = QLineEdit()

        self.bookNameEdit.setMaxLength(10)
        self.bookIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)
        self.addNumEdit.setMaxLength(12)
        self.addNumEdit.setValidator(QIntValidator())

        #self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.bookNameLabel, self.bookNameEdit)
        self.layout.addRow(self.bookIdLabel, self.bookIdEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow(self.addNumLabel, self.addNumEdit)
        #self.layout.addRow(self.addBookButton)
        self.layout.addRow(self.addBookButton)

        font = QFont()
        font.setFamily("Candara")
        font.setPixelSize(20)
        #self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.bookNameLabel.setFont(font)
        self.bookIdLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)
        self.addNumLabel.setFont(font)

        self.bookNameEdit.setFont(font)
        self.bookIdEdit.setFont(font)
        self.authNameEdit.setFont(font)
        self.publisherEdit.setFont(font)
        self.publishTime.setFont(font)
        self.categoryComboBox.setFont(font)
        self.addNumEdit.setFont(font)

        font.setPixelSize(16)
        self.addBookButton.setFont(font)
        self.addBookButton.setFixedHeight(32)
        self.addBookButton.setFixedWidth(280)
        self.addBookButton.setStyleSheet("background-color:rgb(32, 208, 194);\n"
"color:white;")

        #self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.addBookButton.clicked.connect(self.addBookButtonCicked)

    def addBookButtonCicked(self):
        bookName = self.bookNameEdit.text()
        bookId = self.bookIdEdit.text()
        authName = self.authNameEdit.text()
        bookCategory = self.categoryComboBox.currentText()
        publisher = self.publisherEdit.text()
        publishTime = self.publishTime.text()
        addBookNum = self.addNumEdit.text()
        if (
                bookName == "" or bookId == "" or authName == "" or bookCategory == "" or publisher == "" or publishTime == "" or addBookNum == ""):
            print(QMessageBox.warning(self, "Warning", "Some fields are empty", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            addBookNum = int(addBookNum)
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('./db/FBLAE-Book2dbebook.db')
            db.open()
            query = QSqlQuery()
            sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
            query.exec_(sql)
            if (query.next()):
                sql = "UPDATE Book SET NumStorage=NumStorage+%d,NumCanBorrow=NumCanBorrow+%d WHERE BookId='%s'" % (
                    addBookNum, addBookNum, bookId)
            else:
                sql = "INSERT INTO book VALUES ('%s','%s','%s','%s','%s','%s',%d,%d,0)" % (
                    bookName, bookId, authName, bookCategory, publisher, publishTime, addBookNum, addBookNum)
            query.exec_(sql)
            db.commit()
            timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            sql = "INSERT INTO buyordrop VALUES ('%s','%s',1,%d)" % (bookId, timenow, addBookNum)
            query.exec_(sql)
            db.commit()
            print(QMessageBox.information(self, "Information", "Book added!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_book_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.bookNameEdit.clear()
        self.bookIdEdit.clear()
        self.authNameEdit.clear()
        self.addNumEdit.clear()
        self.publisherEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./rsc/manage_ebooks_button.png"))
    mainMindow = addBookDialog()
    mainMindow.show()
    sys.exit(app.exec_())

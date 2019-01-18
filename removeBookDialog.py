import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import time


class dropBookDialog(QDialog):
    drop_book_successful_signal=pyqtSignal()

    def __init__(self, parent=None):
        super(dropBookDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Remove Books")

    def setUpUI(self):
        BookCategory = ["Technology", "Social Science", "Politics", "Law", "Military", "Economics", "Culture", "Education", "Physical Education", "Language Arts", "Arts", "History"
            , "Geography", "Astronomy", "Biology", "Medicine", "Philosophy"]
        self.resize(300, 285)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.bookNameLabel = QLabel("Book Name:")
        self.bookIdLabel = QLabel("Book Code:")
        self.authNameLabel = QLabel("Author:")
        self.categoryLabel = QLabel("Category:")
        self.publisherLabel = QLabel("Publisher:")
        self.publishDateLabel = QLabel("Publish Date:")
        self.dropNumLabel = QLabel("Remove Amount:")

        self.dropBookButton = QPushButton("Remove")

        self.bookNameEdit = QLineEdit()
        self.bookIdEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.addItems(BookCategory)
        self.publisherEdit = QLineEdit()
        self.publishTime = QLineEdit()
        # self.publishDateEdit = QLineEdit()
        self.dropNumEdit = QLineEdit()

        self.bookNameEdit.setMaxLength(10)
        self.bookIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)
        self.dropNumEdit.setMaxLength(12)
        self.dropNumEdit.setValidator(QIntValidator())

        self.layout.addRow(self.bookNameLabel, self.bookNameEdit)
        self.layout.addRow(self.bookIdLabel, self.bookIdEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow(self.dropNumLabel, self.dropNumEdit)
        self.layout.addRow(self.dropBookButton)

        font = QFont()
        font.setFamily("Candara")
        font.setPixelSize(20)
        font.setPixelSize(14)
        self.bookNameLabel.setFont(font)
        self.bookIdLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)
        self.dropNumLabel.setFont(font)

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
        self.dropNumEdit.setFont(font)

        font.setPixelSize(16)
        self.dropBookButton.setFont(font)
        self.dropBookButton.setFixedHeight(32)
        self.dropBookButton.setFixedWidth(280)
        self.dropBookButton.setStyleSheet("background-color:rgb(255, 117, 124);\n"
"color:white;")
        self.layout.setVerticalSpacing(10)

        self.dropBookButton.clicked.connect(self.dropBookButtonClicked)
        self.bookIdEdit.textChanged.connect(self.bookIdEditChanged)

    def bookIdEditChanged(self):
        bookId = self.bookIdEdit.text()
        if (bookId == ""):
            self.bookNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.dropNumEdit.clear()
            self.publishTime.clear()
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/LibraryManagement.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
        query.exec_(sql)

        if (query.next()):
            self.bookNameEdit.setText(query.value(0))
            self.authNameEdit.setText(query.value(2))
            self.categoryComboBox.setCurrentText(query.value(3))
            self.publisherEdit.setText(query.value(4))
            self.publishTime.setText(query.value(5))
        return

    def dropBookButtonClicked(self):
        bookId = self.bookIdEdit.text()
        dropNum = 0
        if (self.dropNumEdit.text() == ""):
            print(QMessageBox.warning(self, "Warning", "Please don't leave empty fields!"), QMessageBox.Yes, QMessageBox.Yes)
            return
        dropNum = int(self.dropNumEdit.text())
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/FBLAE-Book2dbebook.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
        query.exec_(sql)
        if (query.next()):
            if (dropNum > query.value(7) or dropNum < 0):
                print(QMessageBox.warning(self, "Warning", "You can only remove %d book(s)，请检查输入" % (query.value(7)), QMessageBox.Yes,
                                          QMessageBox.Yes))
                return

        if (dropNum == query.value(6)):
            sql = "DELETE  FROM Book WHERE BookId='%s'" % (bookId)
        else:
            sql = "UPDATE BOOK SET NumStorage=NumStorage-%d,NumCanBorrow=NumCanBorrow-%d WHERE BookId='%s'" % (
                dropNum, dropNum, bookId)
        query.exec_(sql)
        db.commit()

        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "INSERT INTO buyordrop VALUES ('%s','%s',0,%d)" % (bookId, timenow, dropNum)
        query.exec_(sql)
        db.commit()
        print(QMessageBox.information(self, "Information", "Book successfully removed", QMessageBox.Yes, QMessageBox.Yes))
        self.drop_book_successful_signal.emit()
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./rsc/manage_ebooks_button.png"))
    mainMindow = dropBookDialog()
    mainMindow.show()
    sys.exit(app.exec_())

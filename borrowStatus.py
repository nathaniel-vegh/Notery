import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *


class BorrowStatusViewer(QWidget):
    def __init__(self, studentId):
        super(BorrowStatusViewer, self).__init__()
        self.resize(700, 500)
        self.studentId = studentId
        self.setWindowTitle("Borrow Status")
        self.setUpUI()

    def setUpUI(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./db/FBLAE-Book2dbebook.db')
        self.db.open()
        self.layout = QVBoxLayout(self)
        self.borrowedLabel = QLabel("Not Returned:")
        self.returnedLabel = QLabel("Returned:")
        self.borrowedLabel.setFixedHeight(32)
        self.borrowedLabel.setFixedWidth(120)
        self.returnedLabel.setFixedHeight(32)
        self.returnedLabel.setFixedWidth(120)
        font = QFont()
        font.setFamily("Candara")
        font.setPixelSize(18)
        self.borrowedLabel.setFont(font)
        self.returnedLabel.setFont(font)

        self.borrowedTableView = QTableView()
        self.borrowedTableView.horizontalHeader().setStretchLastSection(True)
        self.borrowedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.borrowedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.returnedTableView = QTableView()
        self.returnedTableView.horizontalHeader().setStretchLastSection(True)
        self.returnedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.returnedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.borrowedQueryModel = QSqlQueryModel()
        self.returnedQueryModel = QSqlQueryModel()
        self.borrowedTableView.setModel(self.borrowedQueryModel)
        self.returnedTableView.setModel(self.returnedQueryModel)
        self.borrowedQuery()
        self.borrowedQueryModel.setHeaderData(0, Qt.Horizontal, "Book Name")
        self.borrowedQueryModel.setHeaderData(1, Qt.Horizontal, "Book Code")
        self.borrowedQueryModel.setHeaderData(2, Qt.Horizontal, "Author")
        self.borrowedQueryModel.setHeaderData(3, Qt.Horizontal, "Category")
        self.borrowedQueryModel.setHeaderData(4, Qt.Horizontal, "Publisher")
        self.borrowedQueryModel.setHeaderData(5, Qt.Horizontal, "Publish Date")
        self.borrowedQueryModel.setHeaderData(6, Qt.Horizontal, "Borrow Date")

        self.returnedQuery()
        self.returnedQueryModel.setHeaderData(0, Qt.Horizontal, "Book Name")
        self.returnedQueryModel.setHeaderData(1, Qt.Horizontal, "Book Code")
        self.returnedQueryModel.setHeaderData(2, Qt.Horizontal, "Author")
        self.returnedQueryModel.setHeaderData(3, Qt.Horizontal, "Category")
        self.returnedQueryModel.setHeaderData(4, Qt.Horizontal, "Publisher")
        self.returnedQueryModel.setHeaderData(5, Qt.Horizontal, "Publish Date")
        self.returnedQueryModel.setHeaderData(6, Qt.Horizontal, "Borrow Date")
        self.returnedQueryModel.setHeaderData(7, Qt.Horizontal, "Return Date")

        self.layout.addWidget(self.borrowedLabel)
        self.layout.addWidget(self.borrowedTableView)
        self.layout.addWidget(self.returnedLabel)
        self.layout.addWidget(self.returnedTableView)
        return

    def borrowedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Author,Category,Publisher,PublishTime,BorrowTime FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=1 AND StudentId='%s'" % self.studentId
        self.borrowedQueryModel.setQuery(sql)
        return

    def returnedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Author,Category,Publisher,PublishTime,BorrowTime,ReturnTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=0 AND StudentId='%s'" % self.studentId
        self.returnedQueryModel.setQuery(sql)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    mainMindow = BorrowStatusViewer("0000000001")
    mainMindow.show()
    sys.exit(app.exec_())

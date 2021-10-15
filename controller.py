import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainscreen import Ui_MainWindow
from covid import Covid
from book import Book
'''
this is used to control the main page of the system
Integrate other functions of the system
include MyMainForm; MyCovidForm; MyBookForm
'''
class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

class MyCovidForm(QMainWindow, Covid):
    def __init__(self, parent=None):
        super(MyCovidForm, self).__init__(parent)
        self.setupUi(self)

class MyBookForm(QMainWindow, Book):
    def __init__(self, parent=None):
        super(MyBookForm, self).__init__(parent)
        self.setupUi(self)


# define the structure
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.read_appointment()
    myWin.show()
    covid = MyCovidForm()
    book = MyBookForm()
    book.data_select()
    book.double_click()
    book.confirm()
    myWin.pushButton.clicked.connect(covid.show)
    covid.pushButton.clicked.connect(covid.close)
    covid.pushButton.clicked.connect(book.show)
    book.pushButton_3.clicked.connect(myWin.read_appointment)
    sys.exit(app.exec_())
import sys
import pymysql
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainscreen import Ui_MainWindow
from covid import Covid
from calendar import Calendar

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

class MyCovidForm(QMainWindow, Covid):
    def __init__(self, parent=None):
        super(MyCovidForm, self).__init__(parent)
        self.setupUi(self)

class MyCalendarForm(QMainWindow, Calendar):
    def __init__(self, parent=None):
        super(MyCalendarForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    # s = MainWindow()
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.read_appointment()
    myWin.show()
    covid = MyCovidForm()
    calendar = MyCalendarForm()
    myWin.pushButton.clicked.connect(covid.show)
    covid.pushButton.clicked.connect(covid.close)
    covid.pushButton.clicked.connect(calendar.show)
    calendar.pushButton.clicked.connect(calendar.close)
    sys.exit(app.exec_())
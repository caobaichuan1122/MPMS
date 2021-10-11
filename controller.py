import sys
import maincsreen
import main
from PyQt5.QtWidgets import QApplication, QMainWindow
from maincsreen import Ui_MainWindow
from covid import Covid


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

class MyCovidForm(QMainWindow, Covid):
    def __init__(self, parent=None):
        super(MyCovidForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    # s = MainWindow()
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    s = MyCovidForm()
    myWin.pushButton.clicked.connect(s.show)
    sys.exit(app.exec_())
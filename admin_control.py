import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from admin import Admin

class MyMainForm(QMainWindow, Admin):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    # s = MainWindow()
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.total_appointment()
    myWin.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from admin import Admin
from dashboard import Dashboard

# this class is used to control the admin page
class MyMainForm(QMainWindow, Admin):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

class MyDashboadForm(QMainWindow, Dashboard):
    def __init__(self, parent=None):
        super(MyDashboadForm, self).__init__(parent)
        self.set_ui(self)

# set the structure
if __name__ == "__main__":
    # s = MainWindow()
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    dash = MyDashboadForm
    myWin.total_appointment()
    myWin.pushButton.clicked.connect(dash.show)
    dash.data_select()
    dash.double_click()
    myWin.show()
    sys.exit(app.exec_())
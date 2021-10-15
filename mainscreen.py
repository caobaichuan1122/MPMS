import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# this class is used to define the main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 628)
        MainWindow.setMinimumSize(QtCore.QSize(881, 628))
        MainWindow.setMaximumSize(QtCore.QSize(881, 628))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.Claendar = QtWidgets.QCalendarWidget(self.centralwidget)
        # self.Claendar.setGeometry(QtCore.QRect(310, 50, 511, 391))
        # self.Claendar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        # self.Claendar.setObjectName("Claendar")
        # self.Claendar.setMinimumDate(QtCore.QDate(1900, 1, 1))
        # self.Claendar.setMaximumDate(QtCore.QDate(2099, 12, 31))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 201, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 210, 201, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 350, 201, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 50, 450, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(50)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # this function is used to re-translate the ui
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Monash Patient Management System"))
        self.pushButton.setText(_translate("MainWindow", "Make An Appointment"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel Appointment"))
        self.pushButton_3.setText(_translate("MainWindow", "Check in"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "App_Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "App_Time"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Branch_Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GP_Name"))

    # this function is used to read the appointment information
    def read_appointment(self):
        # connect the sql server
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        sql = "SELECT * FROM Patient_App_Info;"
        cur.execute(sql)
        data = cur.fetchall()
        try:
            for data_row in range(50):
                for data_column in range(4):
                    self.tableWidget.setItem(data_row, data_column, QtWidgets.QTableWidgetItem(str(data[data_row][data_column])))
        except:
            pass
        cur.close()
        conn.close()
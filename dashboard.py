import time
from datetime import datetime
from datetime import date
import pymysql
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Dashboard(object):
    # def __init__(self, central_widget, push_button, table_widget1, table_widget2, table_widget3,
    #              menu_bar, status_bar, double_click):
    #     self.central_widget = central_widget
    #     self.push_button = push_button
    #     self.table_widget1 = table_widget1
    #     self.table_widget2 = table_widget2
    #     self.table_widget3 = table_widget3
    #     self.menu_bar = menu_bar
    #     self.status_bar = status_bar
    #     self.double_click = double_click

    def set_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1151, 694)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget)

        self.push_button = QtWidgets.QPushButton(self.central_widget)
        self.push_button.setGeometry(QtCore.QRect(480, 550, 251, 61))
        self.push_button.setObjectName("push_button")

        self.table_widget1 = QtWidgets.QTableWidget(self.central_widget)
        self.table_widget1.setGeometry(QtCore.QRect(20, 60, 251, 431))
        self.table_widget1.setObjectName("table_widget1")
        self.table_widget1.setColumnCount(1)
        self.table_widget1.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget1.setHorizontalHeaderItem(0, item)
        self.table_widget1.horizontalHeader().setStretchLastSection(True)

        self.table_widget2 = QtWidgets.QTableWidget(self.central_widget)
        self.table_widget2.setGeometry(QtCore.QRect(300, 60, 251, 431))
        self.table_widget2.setObjectName("table_widget2")
        self.table_widget2.setColumnCount(1)
        self.table_widget2.setRowCount(30)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget2.setHorizontalHeaderItem(0, item)
        self.table_widget2.horizontalHeader().setStretchLastSection(True)

        self.table_widget3 = QtWidgets.QTableWidget(self.central_widget)
        self.table_widget3.setGeometry(QtCore.QRect(580, 60, 251, 431))
        self.table_widget3.setObjectName("table_widget3")
        self.table_widget3.setColumnCount(1)
        self.table_widget3.setRowCount(30)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget3.setHorizontalHeaderItem(0, item)
        self.table_widget3.horizontalHeader().setStretchLastSection(True)

        self.table_widget4 = QtWidgets.QTableWidget(self.central_widget)
        self.table_widget4.setGeometry(QtCore.QRect(860, 60, 251, 431))
        self.table_widget4.setObjectName("table_widget4")
        self.table_widget4.setColumnCount(1)
        self.table_widget4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget4.setHorizontalHeaderItem(0, item)
        self.table_widget4.horizontalHeader().setStretchLastSection(True)

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1151, 23))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        self.push_button.setText(_translate("main_window", "Finish"))
        item = self.table_widget1.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Branch Name"))
        item = self.table_widget2.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Start Date"))
        item = self.table_widget3.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "End Date"))
        item = self.table_widget4.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Number of People"))

    # print clinic name
    def data_select(self):
        conn = pymysql.connect(host='34.129.105.0',
                               user='Team27',
                               password='Team_27_yu',
                               db='team27',
                               port=3306,
                               charset='utf8')
        cur = conn.cursor()

        sql = "SELECT Branch_Name FROM Branch"
        cur.execute(sql)
        data = cur.fetchall()
        data1 = []
        try:
            for i in range(20):
                data1.append(data[i][0])
        except:
            pass

        data1_set = list(set(data))
        data1_set.sort()
        try:
            for data_row in range(30):
                self.table_widget1.setItem(data_row, 0, QtWidgets.QTableWidgetItem(str(data1_set[data_row][0])))
        except:
            pass
        cur.close()
        conn.close()

    # def get_branch_date(self):
    #     self.branch_date=[]
    #     # return self.branch_date

    # select clinic and print start date
    def button(self):
        self.table_widget3.clearContents()
        self.table_widget2.clearContents()
        conn = pymysql.connect(host='34.129.105.0',
                               user='Team27',
                               password='Team_27_yu',
                               db='team27',
                               port=3306,
                               charset='utf8')
        cur = conn.cursor()

        for i in self.table_widget1.selectedItems():
            self.double_click = i.text()

        sql = 'Select Branch_Name, App_Date FROM Branch b, Appointment a WHERE b.Id = a.Branch_Id; '
        cur.execute(sql)
        data_branch = cur.fetchall()
        # complete data of appointment branch and date
        self.branch_date = []

        try:
            for i in data_branch:
                if i[0] == self.double_click:
                    self.branch_date.append(i)
        except:
            pass
        # set of branch and dates
        branch_date_set = list(set(self.branch_date))
        branch_date_set.sort()

        try:
            for i in range(30):
                # print out start date on second table
                self.table_widget2.setItem(i, 0, QtWidgets.QTableWidgetItem(str(branch_date_set[i][1])))
        except:
            pass
        cur.close()
        conn.close()

    # print end date after selecting start date
    def button2(self):
        self.table_widget3.clearContents()
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()

        sql = 'Select Branch_Name, App_Date FROM Branch b, Appointment a WHERE b.Id = a.Branch_Id; '
        cur.execute(sql)
        data_branch = cur.fetchall()
        # complete data of appointment branch and date
        # branch_date = []

        try:
            for i in data_branch:
                if i[0] == self.double_click:
                    self.branch_date.append(i)
        except:
            pass

        for i in self.table_widget2.selectedItems():
            self.double_click = i.text()

        # list of all possible appointments and dates after start dates
        branch_end = []
        selected_date = datetime.strptime(self.double_click, "%Y-%m-%d").date()
        print(selected_date)
        try:
            # print(self.branch_date)
            for i in self.branch_date:
                if i[1] >= selected_date:
                    branch_end.append(i)
                # print(i[1] >= selected_date)
        except:
            pass

        # print(branch_end)
        # unique list of appointments and dates
        branch_end_set = list(set(branch_end))
        branch_end_set.sort()
        # print(branch_end_set)

        try:
            for i in range(30):
                # print out end date on third table
                self.table_widget3.setItem(i, 0, QtWidgets.QTableWidgetItem(str(branch_end_set[i][1])))
        except:
            pass
        cur.close()
        conn.close()

    # select end date and print number of people
    def button3(self):
        self.table_widget4.clearContents()
        branch_end = self.double_click1
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()

        sql = 'Select Branch_Name, cast(App_Date as char) FROM Branch b, Appointment a WHERE b.Id = a.Branch_Id; '
        cur.execute(sql)
        data_branch = cur.fetchall()
        final_dates = []
        try:
            for i in data_branch:
                if i[1] <= branch_end[0]:
                    final_dates.append(i[1])
        except:
            pass

        num_people = len(final_dates)

        self.table_widget4.setItem(0,0,QtWidgets.QTableWidgetItem(str((num_people))))

    def get_date(self):
        self.double_click1 = []
        for i in self.table_widget3.selectedItems():
            double_click = i.text()
            self.double_click1.append(double_click)
        return self.double_click1

    def double_click(self):
        self.table_widget1.clicked.connect(self.button)
        self.table_widget2.clicked.connect(self.button2)
        self.table_widget3.clicked.connect(self.get_date)
        self.table_widget3.clicked.connect(self.button3)

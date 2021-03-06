import random

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

'''
this function is used to make a appointment
'''
class Book(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 694)
        MainWindow.setMinimumSize(QtCore.QSize(1151, 694))
        MainWindow.setMaximumSize(QtCore.QSize(1151, 694))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 550, 251, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 550, 251, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 60, 256, 431))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(300, 60, 256, 431))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(860, 60, 256, 211))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_8.setGeometry(QtCore.QRect(860, 280, 256, 211))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(1)
        self.tableWidget_8.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(580, 60, 256, 211))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(30)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(580, 280, 256, 211))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1151, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # this is used to re-translate the ui
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Monash Patient Management System"))
        self.pushButton_3.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_2.setText(_translate("MainWindow", "Select"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Branch Name"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "GP Name"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Branch_Name"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Open_hours"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget_5.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Street"))
        item = self.tableWidget_5.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Suburb"))
        item = self.tableWidget_5.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Postcode"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Branch Information"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Branch Unavailable Time"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Available Date"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Available Time"))

    # this function is used to select the data
    def data_select(self):
        # connect the sql server
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        sql = "SELECT Branch_Name FROM Branch;"
        cur.execute(sql)
        data = cur.fetchall()
        data1 = []
        try:
            # append the data to the data1
            for i in range(20):
                data1.append(data[i][0])
        except:
            pass
        data1 = list(set(data))
        data1.sort()
        try:
            for data_row in range(30):
                self.tableWidget_3.setItem(data_row, 0, QtWidgets.QTableWidgetItem(str(data1[data_row][0])))
        except:
            pass
        cur.close()
        conn.close()

    # this function is used to define the button which is used to select Branch_Name,Opening_hours,Phone,Street,Suburb,Postcode from Branch
    def button(self):
        # connect the sql server
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        # use a for loop to check the items
        for i in self.tableWidget_3.selectedItems():
            double_click = i.text()
        sql = 'select Branch_Name,Opening_hours,Phone,Street,Suburb,Postcode from Branch; '
        cur.execute(sql)
        data_branch = cur.fetchall()
        Branch_inf = []
        try:
            # store the branch info to the list
            for i in data_branch:
                if i[0] == double_click:
                    Branch_inf.append(i)
        except:
            pass
        try:
            for i in range(30):
                for j in range(6):
                    self.tableWidget_5.setItem(i, j, QtWidgets.QTableWidgetItem(str(Branch_inf[i][j])))
        except:
            pass
        cur.close()
        conn.close()

    # this function is used to define the button2 which get and display the GP information
    def button2(self):
        self.tableWidget_6.clearContents()
        self.tableWidget_7.clearContents()
        # connect the sql server
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        # use a for loop to check the items
        for i in self.tableWidget_3.selectedItems():
            double_click = i.text()
        sql = 'select Branch_Name,Gname from Branch b,GP g where b.Id=g.Branch_Id; '
        cur.execute(sql)
        data_GP = cur.fetchall()
        gp_name = []
        try:
            # get and store the GP info
            for i in data_GP:
                if i[0] == double_click:
                    gp_name.append(i[1])
        except:
            pass

        try:
            for i in range(30):
                for j in gp_name:
                    self.tableWidget_4.setItem(i, 0, QtWidgets.QTableWidgetItem(str(gp_name[i])))
        except:
            pass
        cur.close()
        conn.close()

    # this function is used to define the button2 which get and display the GP_timetable information
    def button3(self):
        self.tableWidget_6.clearContents()
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        for i in self.tableWidget_4.selectedItems():
            double_click = i.text()
        sql = 'select g.Gname,CAST(gt.App_Date AS CHAR) AS App_Date from GP_timetable gt,GP g where g.Id=gt.GP_Id;'
        cur.execute(sql)
        data_app = cur.fetchall()
        gp_app_date = []
        try:
            for i in data_app:
                if i[0] == double_click:
                    gp_app_date.append(i[1])
        except:
            pass
        gp_app_date_set = list(set(gp_app_date))
        gp_app_date_set.sort()
        try:
            for i in range(500):
                    self.tableWidget_6.setItem(i,0, QtWidgets.QTableWidgetItem(str(gp_app_date_set[i])))
        except:
            pass
        cur.close()
        conn.close()

    # this function is used to define the button2 which get and display the available time of GP
    def button4(self):
        self.tableWidget_7.clearContents()
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        for i in self.tableWidget_6.selectedItems():
            double_click = i.text()
        sql = 'select CAST(App_Date AS CHAR),CAST(App_Time AS CHAR) from GP_timetable;'
        cur.execute(sql)
        data_app = cur.fetchall()
        gp_app_time = []
        try:
            for i in data_app:
                if i[0] == str(double_click):
                    gp_app_time.append(i[1])
        except:
            pass
        gp_app_time_set = list(set(gp_app_time))
        gp_app_time_set.sort()
        try:
            for i in range(500):
                        self.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(gp_app_time_set[i])))
        except:
            pass
        cur.close()
        conn.close()


    def button5(self):
        self.tableWidget_8.clearContents()
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        for i in self.tableWidget_3.selectedItems():
            double_click = i.text()
        sql = 'select b.Branch_Name,CAST(bu.Branch_Datetime AS CHAR) AS Branch_Datetime from Branch b,Branch_unavailable_time bu where b.Id=bu.Branch_Id;'
        cur.execute(sql)
        data_GP = cur.fetchall()
        gp_name = []
        try:
            for i in data_GP:
                if i[0] == double_click:
                    gp_name.append(i[1])
        except:
            pass

        try:
            for i in range(30):
                for j in gp_name:
                    self.tableWidget_8.setItem(i, 0, QtWidgets.QTableWidgetItem(str(gp_name[i])))
        except:
            pass
        cur.close()
        conn.close()

    def double_click(self):
        self.tableWidget_3.clicked.connect(self.button)
        self.tableWidget_3.clicked.connect(self.button5)
        self.tableWidget_3.clicked.connect(self.button2)
        self.tableWidget_4.clicked.connect(self.button3)
        self.tableWidget_6.clicked.connect(self.button4)
        self.tableWidget_3.clicked.connect(self.app_info)
        self.tableWidget_4.clicked.connect(self.app_info)
        self.tableWidget_6.clicked.connect(self.app_info)
        self.tableWidget_7.clicked.connect(self.app_info)
        # self.pushButton_2.clicked.connect(self.verify)

    def app_info(self):
        self.patient_info = []
        for i in self.tableWidget_3.selectedItems():
            double_click = i.text()
            self.patient_info.append(double_click)
        for i in self.tableWidget_4.selectedItems():
            double_click1 = i.text()
            self.patient_info.append(double_click1)
        for i in self.tableWidget_6.selectedItems():
            double_click2 = i.text()
            self.patient_info.append(double_click2)
        for i in self.tableWidget_7.selectedItems():
            double_click3 = i.text()
            self.patient_info.append(double_click3)
        return self.patient_info

    # this function is used to save the info of user selected
    def save_info(self):
        patient_info = self.patient_info
        conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        cur1 = conn.cursor()
        if len(patient_info) == 4:
            sql = "INSERT INTO Patient_App_Info (Branch_Name, GP_Name, App_Date, App_Time) VALUES ('%s','%s','%s','%s')" % (
                    patient_info[0],patient_info[1],patient_info[2],patient_info[3])
            cur.execute(sql)
            conn.commit()
            QtWidgets.QMessageBox.about(self, 'notification','Congratulations, the appointment is successful!')
        elif len(patient_info) == 3:
            QtWidgets.QMessageBox.about(self, 'notification', 'Please select date and time!')
        elif len(patient_info) == 2:
            QtWidgets.QMessageBox.about(self, 'notification', 'Please select date and time!')
        elif len(patient_info) == 1:
            sql = 'SELECT g.Id,b.Branch_name,g.Gname,any_value(CAST(gt.App_Date AS CHAR)),any_value(CAST(gt.App_Time AS CHAR)) ' \
                  'FROM GP g join GP_timetable gt join Branch b where g.Id = gt.GP_Id and b.Id = g.Branch_Id group by g.Id order by g.Id desc limit 1;'
            cur1.execute(sql)
            total_app = cur1.fetchall()
            sql = "INSERT INTO Patient_App_Info (Branch_Name, GP_Name, App_Date, App_Time) VALUES ('%s','%s','%s','%s')" % (
                total_app[0][1], total_app[0][2], total_app[0][3], total_app[0][4])
            cur1.execute(sql)
            conn.commit()
            QtWidgets.QMessageBox.about(self, 'notification',
                                        'If you do not select GP, date or time, the system will assign you the GP with the least appointment time.')
        cur.close()
        conn.close()

    def confirm(self):
        self.pushButton_2.clicked.connect(self.save_info)


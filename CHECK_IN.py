import time
from datetime import date
import pymysql


def clear_previous():
    conn = pymysql.connect(host='34.129.105.0',
                           user='Team27',
                           password='Team_27_yu',
                           db='team27',
                           port=3306,
                           charset='utf8')
    cursor = conn.cursor()

    sql = " UPDATE `Appointment` SET `Check_in` = 0 WHERE `App_Date` = current_date() " \
          "AND `App_Time` < now() - interval 45 minute "
    cursor.execute(sql)
    sql_2 = "UPDATE `Appointment` SET `Check_in` = 0 WHERE `App_Date` < current_date()"
    cursor.execute(sql_2)


def filter_appointment():
    conn = pymysql.connect(host='34.129.105.0',
                           user='Team27',
                           password='Team_27_yu',
                           db='team27',
                           port=3306,
                           charset='utf8')
    cursor = conn.cursor()

    # filter the appointments that are eligible for signing in
    sql = "SELECT * FROM `Appointment` WHERE `App_Date` = current_date() " \
          "AND `App_Time` < now() + interval 10 minute AND `Patient_Id` = '1'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


def check_in():

    conn = pymysql.connect(host='34.129.105.0',
                           user='Team27',
                           password='Team_27_yu',
                           db='team27',
                           port=3306,
                           charset='utf8')
    cursor = conn.cursor()

    clear_previous()

    filter_appointment()

    # change the status of check_in to 1
    sql = "UPDATE `Appointment` SET Check_in = '1' WHERE `App_Date` = current_date() " \
          "AND `App_Time` < now() + interval 10 minute AND `Patient_Id` = '1' "
    cursor.execute(sql)
    result = cursor.fetchall()

    sql = "SELECT COUNT(*) - 1 FROM `Appointment` WHERE `Check_in` = '1'"
    cursor.execute(sql)
    result = cursor.fetchone()
    # return number of people in front of you
    num_people = str(result[0])
    print("Checked in successfully. There are " + num_people +
          " people in front of you, please wait for our staff to call you.")


    conn.close()
    cursor.close()


# check_in()
clear_previous()


import pymysql
import datetime


# timedelta to time
def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


# clear previous check_in record
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
    cursor.execute('UPDATE Appointment SET Check_in = 0 WHERE App_Date < current_date()')
    conn.commit()


# print out queue
def print_queue():

    conn = pymysql.connect(host='34.129.105.0',
                           user='Team27',
                           password='Team_27_yu',
                           db='team27',
                           port=3306,
                           charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT COUNT(*) - 1 FROM `Appointment` WHERE `Check_in` = '1'"
    cursor.execute(sql)
    result = cursor.fetchone()
    # return number of people in front of you
    num_people = str(result[0])
    print("Checked in successfully. There are " + num_people +
          " people in front of you, please wait for our staff to call you.")


def appointment_verify(app_id):

    clear_previous()

    conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306,
                           charset='utf8')
    cur = conn.cursor()

    cur.execute('SELECT App_Time, App_Date FROM Appointment WHERE Appointment.Id = %s' % app_id)

    result_time, result_date = cur.fetchone()

    if result_date is None and result_time is None:
        print('error',' Id NOT FOUND!')

    else:

        now = datetime.datetime.now()

        hours, minutes, seconds = convert_timedelta(result_time)

        time_converted = datetime.time(hour=hours, minute=minutes, second=seconds)

        date_time = datetime.datetime.combine(date = result_date, time = time_converted)

        check_in = (now - date_time)
        diff = check_in.total_seconds() / 60

        if diff <= 10:
            cur.execute('UPDATE Appointment SET Check_In = 1 WHERE Appointment.Id = %s' % app_id)
            print_queue()
        else:
            print("Failed to check in, please contact staff for instruction!")
        conn.commit()



# appointment_verify(1)
# clear_previous()
# print_queue()










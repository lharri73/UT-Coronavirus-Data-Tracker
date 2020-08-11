from matplotlib import pyplot as plt
import mysql.connector
import datetime
import numpy as np

def main():
    mydb = mysql.connector.connect(
        host="34.75.230.71",
        user="coronaReader",
        password="superSecretPassword1234",
        database="corona_info"
    )
    cnx = mydb.cursor(buffered=True)
    cnx.execute("SELECT Date, Students, Faculty, Staff FROM corona_data")

    dates = []
    students = []
    faculty = []
    staff = []
    for (Date, Students, Faculty, Staff) in cnx:
        dates.append(Date)
        students.append(Students)
        faculty.append(Faculty)
        staff.append(Staff)
    cnx.close()
    mydb.close()

    stu, = plt.plot(dates, students, label="Students")
    sta, = plt.plot(dates, staff, label="Staff")
    fac, = plt.plot(dates, faculty, label="Faculty")
    mvin = plt.axvline(x=datetime.datetime(2020,8,9), label="Start Of Move-ins", color="r")

    noDat = plt.axvspan(datetime.datetime(2020,8,10,19), datetime.datetime(2020,8,11,12), color='yellow', alpha=0.5)

    plt.gcf().autofmt_xdate()
    plt.legend((stu,sta, fac, mvin, noDat), ("Students", "Staff", "Faculty", "Start Of Move-ins", "No Data"), ncol=2, loc="center left")

    plt.title('Coronavirus Cases At UT')
    plt.ylabel('Cases')
    plt.xlabel('Date (UTC)')
    plt.yticks(np.arange(0.0, max([max(students), max(staff), max(faculty)])+1, 1.0))
    plt.show()


if __name__ == "__main__":
    main()

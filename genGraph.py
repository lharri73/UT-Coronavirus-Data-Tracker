from matplotlib import pyplot as plt
import mysql.connector
import datetime

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

    plt.plot(dates, students, label="Students")
    plt.plot(dates, staff, label="Staff")
    plt.plot(dates, faculty, label="Faculty")
    plt.axvline(x=datetime.datetime(2020,8,9), label="Start Of Move-ins", color="r")
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.title('Coronavirus Cases At UT')
    plt.ylabel('Cases')
    plt.xlabel('Date')
    plt.show()


if __name__ == "__main__":
    main()

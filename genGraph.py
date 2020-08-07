from matplotlib import pyplot as plt
import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host="34.75.230.71",
        user="root",
        password="ALANFisher",
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
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.title('Coronavirus Cases Tt UT')
    plt.ylabel('Cases')
    plt.xlabel('Date')
    plt.show()


if __name__ == "__main__":
    main()

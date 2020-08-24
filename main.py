import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from mysql.connector import ClientFlag

def get_page():
    URL = "https://veoci.com/veoci/p/form/4jmds5x4jj4j"
    page = requests.get(URL)
    stringStuff = page.content.decode("unicode_escape")
    prog = re.compile(r"Students.*?>(\d+)<.*?Faculty.*?>(\d+)<.*?Staff.*?>(\d)<")
    result = re.search(prog, stringStuff)
    students = result.group(1)
    faculty = result.group(2)
    staff = result.group(3)

    print("Students : {}\nFaculty: {}\nStaff: {}".format(students,faculty,staff))
    insert_sql(students, faculty, staff)
    
def insert_sql(students, faculty, staff):
    mydb = mysql.connector.connect(
        host="34.75.230.71",
        user="coronaDataEditor",
        password="*****************",
#        client_flags=[ClientFlag.SSL],
#        ssl_ca="server-ca.pem",
#        ssl_cert="client-cert.pem",
#        ssl_key="client-key.pem",
        database="corona_info"
    )
    cnx = mydb.cursor(buffered=True)
    cnx.execute("CREATE TABLE IF NOT EXISTS corona_data(\
        id INT AUTO_INCREMENT PRIMARY KEY, \
        Date DATETIME DEFAULT NOW(), \
        Students INT, \
        Faculty INT, \
        Staff INT \
    ); ")
    cnx.execute("INSERT INTO corona_data (Students, Faculty, Staff) VALUES({}, {}, {});".format(
        int(students),
        int(faculty),
        int(staff)
    ))
    cnx.close()
    mydb.commit()
    mydb.close()

if __name__ == "__main__":
    get_page()

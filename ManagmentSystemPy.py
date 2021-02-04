#Chrisitian Escobarete & Moe
import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(
        user="ms_user",
        password="manageuser",
        host="127.0.0.1",
        database="ManageEmp")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid Credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print("Cannot connect to database:", err)

else:
    employee_cursor = db_connection.cursor()
    employee_query = ("SELECT eID, name, startTime, endTime "
                      "FROM Employee ")

    employee_cursor.execute(employee_query)

    for row in employee_cursor.fetchall():
        print("\nEmployee ID: {} - Name: {} - Start: {} - End: {} "
              .format(row[0], row[1], row[2], row[3]))

    employee_cursor.close()
    db_connection.close()
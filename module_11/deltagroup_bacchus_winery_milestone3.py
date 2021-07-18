"""
    Andrew Schaefer, Jennifer Thomas, Milo Blake, Shane Fox, Caleb Mastromonaco
    Date: 7/17/2021
    CSD310 - Module 11 - Milestone 3
"""


""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "WanderLust#0588#",
    "host": "127.0.0.1",
    "database": "bacchus",
    "raise_on_warnings": True
}

""" Test connection to mysql"""
try:
    db = mysql.connector.connect(**config) # connect to the bacchus database 

    mycursor = db.cursor()

    # Report #1, get Supplier_ID, Supplier_name, then expected and actual dates per month.
    mycursor.execute("SELECT supplier_name, deliveries.supplier_id, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, decem FROM supplier, deliveries WHERE supplier.supplier_id = deliveries.supplier_id")
    result = mycursor.fetchall()

    print("--DISPLAYING REPORT ONE--\n")
    for x in result:
        print("Supplier_ID: {}" .format(x[1]))
        print("Supplier Name: {}" .format(x[0]))
        print("January: {}" .format(x[2]))
        print("February: {}" .format(x[3]))
        print("March: {}" .format(x[4]))
        print("April: {}" .format(x[5]))
        print("May: {}" .format(x[6]))
        print("June: {}" .format(x[7]))
        print("July: {}" .format(x[8]))
        print("August: {}" .format(x[9]))
        print("September: {}" .format(x[10]))
        print("October: {}" .format(x[11]))
        print("November: {}" .format(x[12]))
        print("December: {}\n" .format(x[13]))

        mycursor.execute("SELECT wine.wine_name, distributor_name, location, bottles_sold FROM distributor, wine WHERE distributor.distributor_id = wine.distributor_id")
        result = mycursor.fetchall()

    # Report #2 showing what wines are sold where and in what quantity
    print("--DISPLAYING REPORT TWO--\n")
    for x in result:
        print("Wine: {}" .format(x[0]))
        print("Distributor: {}" .format(x[1]))
        print("Location: {}" .format(x[2]))
        print("Bottles Sold: {}\n" .format(x[3]))

    mycursor.execute("SELECT employee_name, q_1, q_2, q_3, q_4 FROM employees")
    result = mycursor.fetchall()

    # Report #3 showing employees and hours worked by quarter.
    print("--DISPLAYING REPORT THREE--\n")
    for x in result:
        print("Name: {}" .format(x[0]))
        print("Q1: {}, Q2: {}, Q3: {}, Q4: {}\n" .format(x[1], x[2], x[3], x[4]))

    input("\n  Press any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
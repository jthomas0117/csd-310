# Delta Group
# Andrew Schaefer, Jennifer Thomas, Milo Blake, Shane Fox, Caleb Mastromonaco
# 7/9/21
# CSD-310
# Module 10.3
# Milestone 2

import mysql.connector
from mysql.connector import errorcode 

# Configures and connects to database
config = {
 "user": "bacchus_user",
 "password": "weare138",
 "host": "127.0.0.1",
 "database": "bacchus",
 "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
mycursor = db.cursor()

# ---TABLE CREATION-------------------------------------------

# Create employees table
sql = "CREATE TABLE employees(employee_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, employee_name varchar(75) NOT NULL, q_1 int NOT NULL, q_2 int NOT NULL, q_3 int NOT NULL, q_4 int NOT NULL)"
mycursor.execute(sql)

# Create distributor table
sql2 = "CREATE TABLE distributor(distributor_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, distributor_name varchar(75) NOT NULL, location varchar(100) NULL, wine_name varchar(75) NOT NULL)"
mycursor.execute(sql2)

# Create supplies table
sql3 = "CREATE TABLE supplies(supply_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, supply_type varchar(75) NOT NULL)"
mycursor.execute(sql3)

# Create wine table
sql4 = "CREATE TABLE wine(wine_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, wine_name varchar(75) NOT NULL, bottles_sold int NOT NULL, distributor_id int NOT NULL)"
mycursor.execute(sql4)

# Create deliveries table
sql5 = "CREATE TABLE deliveries(supplier_id int NOT NULL, jan varchar(100) NULL, feb varchar(100) NULL, mar varchar(100) NULL, apr varchar(100) NULL, may varchar(100) NULL, jun varchar(100) NULL, jul varchar(100) NULL, aug varchar(100) NULL, sep varchar(100) NULL, oct varchar(100) NULL, nov varchar(100) NULL, decem varchar(100) NULL)"
mycursor.execute(sql5)

# Create supplier table
sql6 = "CREATE TABLE supplier(supplier_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, supplier_name varchar(75) NOT NULL, supply_id int NOT NULL)"
mycursor.execute(sql6)

# Add distributor_id foreign key to wine table
sql7 = "ALTER TABLE wine ADD FOREIGN KEY(distributor_id) REFERENCES distributor(distributor_id)"
mycursor.execute(sql7)

# Add supplier_id foreign key to deliveries table
sql8 = "ALTER TABLE deliveries ADD FOREIGN KEY(supplier_id) REFERENCES supplier(supplier_id)"
mycursor.execute(sql8)

# Add supply_id foreign key to supplier table
sql9 = "ALTER TABLE supplier ADD FOREIGN KEY(supply_id) REFERENCES supplies(supply_id)"
mycursor.execute(sql9)

# ---ADD RECORDS-------------------------------------------

# ADDING RECORDS TO EMPLOYEES


sql_insert = "INSERT INTO employees(employee_name, q_1, q_2, q_3, q_4) VALUES (%s, %s, %s, %s, %s)"

val = [
   ("Janet Collins", 481, 476, 480, 491),
   ("Roz Murphy", 480, 475, 480, 490),
   ("Bob Ulrich", 482, 375, 490, 490),
   ("Henry Doyle", 470, 480, 480, 489),
   ("Maria Costanza", 471, 475, 483, 492),
   ("Jessica Murphy", 480, 475, 480, 490),
   ("Andrew Reynolds", 430, 475, 481, 490),
   ("Kareem Campbell", 484, 475, 470, 493),
   ("Ali Boulala", 480, 478, 480, 499),
   ("Dustin Dollin", 481, 475, 480, 490),
   ("Leticia Bufoni", 480, 461, 480, 420),
   ("Tony Hawk", 480, 485, 480, 490),
   ("Elissa Steamer", 480, 475, 480, 490),
   ("Lacey Baker", 480, 480, 480, 490),
   ("Derrik Neff", 480, 475, 480, 490),
   ("Ryan Hall", 480, 475, 430, 490),
   ("Brandon Stokes", 481, 475, 480, 491),
   ("Vilma Gonzales", 480, 485, 426, 490),
   ("Amy Jenson", 480, 487, 480, 492),
   ("Tyrone Jackson", 480, 475, 480, 490),
   ("Shantel Curry", 480, 475, 480, 490),
   ("Felix Argules", 480, 475, 480, 490),
   ("Milton Martinez", 450, 475, 450, 490),
   ("Sam Smith", 480, 474, 489, 490),
   ("Pete Draco", 480, 475, 480, 499)
]
mycursor.executemany(sql_insert, val)
db.commit()

# ADDING RECORDS TO SUPPLIES


sql_insert = "INSERT INTO supplies(supply_id, supply_type) VALUES(%s, %s)"

val = [
   (1, "bottles"),
   (2, "corks"),
   (3, "lables"),
   (4, "boxes"),
   (5, "vats"),
   (6, "tubing")
]
mycursor.executemany(sql_insert, val)
db.commit()

# ADDING RECORDS TO SUPPLIER


sql_insert = "INSERT INTO supplier(supplier_name, supply_id) VALUES(%s, %s)"

val = [
   ("Quality Wine Products", 1),
   ("Quality Wine Products", 2),
   ("Superior Wine Equipment", 3),
   ("Superior Wine Equipment", 4),
   ("Smith Family Wine and More", 5),
   ("Smith Family Wine and More", 6)
]
mycursor.executemany(sql_insert, val)
db.commit()

# ADDING RECORDS TO DELIVERIES


sql_insert = "INSERT INTO deliveries(supplier_id, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, decem) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = [
   (4, "Expected: 011220 Actual: 011020", "Expected: 021020 Actual: 021020", "Expected: 031120 Actual: 032020", "Expected: 041520 Actual: 041620", "Expected: 051420 Actual: 050520", "Expected: 062020 Actual: 061020", "Expected: 071220 Actual: 070820", "Expected: 081720 Actual: 081020", "Expected: 091720 Actual: 091620", "Expected: 101220 Actual: 101020", "Expected: 111220 Actual: 112120", "Expected: 120720 Actual: 121020",),
   (5, "Expected: 010820 Actual: 011020", "Expected: 020420 Actual: 021020", "Expected: 032120 Actual: 033020", "Expected: 041620 Actual: 041620", "Expected: 052020 Actual: 052120", "Expected: 060320 Actual: 061020", "Expected: 070220 Actual: 070420", "Expected: 081120 Actual: 080320", "Expected: 090620 Actual: 091720", "Expected: 100320 Actual: 101920", "Expected: 112120 Actual: 112520", "Expected: 120320 Actual: 121920",),
   (6, "Expected: 011620 Actual: 011620", "Expected: 021520 Actual: 021320", "Expected: 032020 Actual: 031020", "Expected: 042520 Actual: 042620", "Expected: 050420 Actual: 050520", "Expected: 062020 Actual: 061520", "Expected: 071920 Actual: 070920", "Expected: 081520 Actual: 081120", "Expected: 092020 Actual: 090420", "Expected: 100220 Actual: 101120", "Expected: 110220 Actual: 110220", "Expected: 120420 Actual: 121820",),
   (7, "Expected: 011220 Actual: 011020", "Expected: 021020 Actual: 021020", "Expected: 031120 Actual: 032020", "Expected: 041520 Actual: 041620", "Expected: 051420 Actual: 050520", "Expected: 062020 Actual: 061020", "Expected: 071220 Actual: 070820", "Expected: 081720 Actual: 081020", "Expected: 091720 Actual: 091620", "Expected: 101220 Actual: 101020", "Expected: 111220 Actual: 112120", "Expected: 120720 Actual: 121020",),
   (8, "Expected: 012220 Actual: 011920", "Expected: 022220 Actual: 022220", "Expected: 031720 Actual: 031020", "Expected: 042020 Actual: 041520", "Expected: 051320 Actual: 050320", "Expected: 062620 Actual: 060320", "Expected: 071920 Actual: 070920", "Expected: 081420 Actual: 081320", "Expected: 091620 Actual: 091620", "Expected: 101320 Actual: 101320", "Expected: 111520 Actual: 112520", "Expected: 120820 Actual: 121520",),
   (9, "Expected: 011220 Actual: 011020", "Expected: 021020 Actual: 021020", "Expected: 031120 Actual: 032020", "Expected: 041520 Actual: 041620", "Expected: 051420 Actual: 050520", "Expected: 062020 Actual: 061020", "Expected: 071220 Actual: 070820", "Expected: 081720 Actual: 081020", "Expected: 091720 Actual: 091620", "Expected: 101220 Actual: 101020", "Expected: 111220 Actual: 112120", "Expected: 120720 Actual: 121020",)
]
mycursor.executemany(sql_insert, val)
db.commit()

# ADDING RECORDS TO DISTRIBUTOR


sql_insert = "INSERT INTO distributor(distributor_name, location, wine_name) VALUES(%s, %s, %s)"

val = [
   ("Speedy Wine", "Austin, TX", "McMerlot"),
   ("Bringin UR Wine", "Orlando, FL", "Paris in the Summer Cabernet"),
   ("Jackson Wine Distributors", "Sacramento, CA", "Mad Dog 20/20 Chablis"),
   ("Drunken Dist.", "Miami, FL", "Cupcake Chardonnay")
]
mycursor.executemany(sql_insert, val)
db.commit()

# ADDING RECORDS TO WINE


sql_insert = "INSERT INTO wine(wine_name, bottles_sold, distributor_id) VALUES(%s, %s, %s)"

val = [
   ("McMerlot", 272, 1),
   ("Paris in the Summer Cabernet", 140, 2),
   ("Mad Dog 20/20 Chablis", 189, 3),
   ("Cupcake Chardonnay", 439, 4)
]
mycursor.executemany(sql_insert, val)
db.commit()

# ---DISPLAY RECORDS-------------------------------------------

# DISPLAYING SUPPLIES RECORDS
mycursor.execute("SELECT supply_id, supply_type FROM supplies")
result = mycursor.fetchall()

print("\n--DISPLAYING SUPPLIES RECORDS--")
for x in result:
 print("Supply ID: {}" .format(x[0]))
 print("Supply Type: {}" .format(x[1]))

# DISPLAYING SUPPLIER RECORDS
mycursor.execute("SELECT supplier_id, supplier_name, supply_id FROM supplier")
result = mycursor.fetchall()

print("\n--DISPLAYING SUPPLIER RECORDS--")

for x in result:
 print("Supplier ID: {}" .format(x[0]))
 print("Supplier Name: {}" .format(x[1]))
 print("Supply ID: {}" .format(x[2]))

# DISPLAYING EMPLOYEES RECORDS
mycursor.execute("SELECT employee_id, employee_name, q_1, q_2, q_3, q_4 FROM employees")
result = mycursor.fetchall()

print("\n--DISPLAYING EMPLOYEES RECORDS--")
for x in result:
 print("Employee ID: {}" .format(x[0]))
 print("Employee Name: {}" .format(x[1]))
 print("Quarter 1 Hours: {}" .format(x[2]))
 print("Quarter 2 Hours: {}" .format(x[3]))
 print("Quarter 3 Hours: {}" .format(x[4]))
 print("Quarter 4 Hours: {}" .format(x[5]))

# DISPLAYING DELIVERIES RECORDS
mycursor.execute("SELECT supplier_id, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, decem FROM deliveries")
result = mycursor.fetchall()

print("\n--DISPLAYING DELIVERIES RECORDS--")
for x in result:
 print("Supplier ID: {}" .format(x[0]))
 print("January: {}" .format(x[1]))
 print("February: {}" .format(x[2]))
 print("March: {}" .format(x[3]))
 print("April: {}" .format(x[4]))
 print("May: {}" .format(x[5]))
 print("June: {}" .format(x[6]))
 print("July: {}" .format(x[7]))
 print("August: {}" .format(x[8]))
 print("September: {}" .format(x[9]))
 print("October: {}" .format(x[10]))
 print("November: {}" .format(x[11]))
 print("December: {}" .format(x[12]))

# DISPLAYING WINE RECORDS
mycursor.execute("SELECT wine_id, wine_name, bottles_sold, distributor_id FROM wine")
result = mycursor.fetchall()

print("\n--DISPLAYING WINE RECORDS--")
for x in result:
 print("Wine ID: {}" .format(x[0]))
 print("Wine Name/Type: {}" .format(x[1]))
 print("Bottles Sold: {}" .format(x[2]))
 print("Distributor ID: {}" .format(x[3]))

# DISPLAYING DISTRIBUTOR RECORDS 
mycursor.execute("SELECT distributor_id, distributor_name, location, wine_name FROM distributor")
result = mycursor.fetchall()

print("\n--DISPLAYING DISTRIBUTOR RECORDS--")
for x in result:
 print("Distributor ID: {}" .format(x[0]))
 print("Distributor Name: {}" .format(x[1]))
 print("Location: {}" .format(x[2]))
 print("Wine Name: {}" .format(x[3]))
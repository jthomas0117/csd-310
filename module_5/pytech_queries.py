# Jennifer Thomas - CSD 310 - 06/18/21 - Module 5.3
# Pytech queries

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bjm7n.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + str(doc["student_id"]) + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
 
print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

sam = students.find_one({"student_id": 1007})
 
print(" Student ID: " + str(sam["student_id"]) + "\n First Name: " + sam["first_name"] + "\n Last Name: " + sam["last_name"] + "\n")

input("\n\n End of program, press any key to exit... ")
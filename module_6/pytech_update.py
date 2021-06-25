# Jennifer Thomas - CSD 310 - Module 6.2 - 06/25/21
# Pytech update

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bjm7n.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + str(doc["student_id"]) + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

db.students.update_one({"student_id": 1007}, {"$set": {"last_name": "Jones"}})

print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

sam = students.find_one({"student_id": 1007})
 
print(" Student ID: " + str(sam["student_id"]) + "\n First Name: " + sam["first_name"] + "\n Last Name: " + sam["last_name"] + "\n")
 
input("\n\n End of program, press any key to continue... ")
# Jennifer Thomas - CSD 310 - Module 6.3 - 06/25/21
# Pytech delete

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bjm7n.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + str(doc["student_id"]) + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#test document
jim = {
    "student_id": 1010,
    "first_name": "Jim",
    "last_name": "Halpert",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 2.5,
            "start_date": "May 05, 2021",
            "end_date": "December 20, 2021",
            "courses":  [
                {
                    "course_id": 741852,
                    "description": "English 102",
                    "instructor": "Austen",
                    "grade": "C",
                },
                {
                    "course_id": 713842,
                    "description": "Java",
                    "instructor": "James",
                    "grade": "B",
                }
            ]
        }
   ]
}

#insert test document
jim_student_id = students.insert_one(jim).inserted_id

print("\n -- INSERT STATEMENTS -- ") 
print(" Inserted student record into students collection with document_ID " + str(jim_student_id))

print("\n -- DISPLAYING STUDENT TEST DOC --")

jim = students.find_one({"student_id": 1010})
 
print(" Student ID: " + str(jim["student_id"]) + "\n First Name: " + jim["first_name"] + "\n Last Name: " + jim["last_name"] + "\n")

#delete test document
db.students.delete_one({"student_id" : 1010})

updated_student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in updated_student_list:
    print(" Student ID: " + str(doc["student_id"]) + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

input("\n\n End of program, press any key to continue... ")
# Jennifer Thomas - CSD 310 - 06/18/21 - Module 5.3
# Insert three students

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bjm7n.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

sam = {
    "student_id": 1007,
    "first_name": "Sam",
    "last_name": "Smith",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 3.5,
            "start_date": "May 05, 2021",
            "end_date": "December 20, 2021",
            "courses":  [
                {
                    "course_id": 369741,
                    "description": "HTML and CSS",
                    "instructor": "Jones",
                    "grade": "A",
                },
                {
                    "course_id": 147963,
                    "description": "English 101",
                    "instructor": "Sims",
                    "grade": "B",
                }
            ]
        }
   ]
}

phil = {
    "student_id": 1008,
    "first_name": "Philip",
    "last_name": "Marlowe",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 4.0,
            "start_date": "May 05, 2021",
            "end_date": "December 20, 2021",
            "courses":  [
                {
                    "course_id": 971249,
                    "description": "Calculus",
                    "instructor": "Pearson",
                    "grade": "A",
                },
                {
                    "course_id": 349658,
                    "description": "Psychology",
                    "instructor": "Yang",
                    "grade": "A",
                }
            ]
        }
   ]
}


dixon = {
    "student_id": 1009,
    "first_name": "Dixon",
    "last_name": "Steele",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 2.9,
            "start_date": "May 05, 2021",
            "end_date": "December 20, 2021",
            "courses":  [
                {
                    "course_id": 459752,
                    "description": "Literature",
                    "instructor": "Jackson",
                    "grade": "C",
                },
                {
                    "course_id": 341975,
                    "description": "Chemistry",
                    "instructor": "Sanderson",
                    "grade": "D",
                }
            ]
        }
   ]
}

students = db.students

sam_student_id = students.insert_one(sam).inserted_id

print("\n -- INSERT STATEMENTS -- ") 
print(" Inserted student record Sam Spade into students collection with document_ID " + str(sam_student_id))

phil_student_id = students.insert_one(phil).inserted_id

print(" Inserted student record Philip Marlowe into students collection with document_ID " + str(phil_student_id))

dixon_student_id = students.insert_one(dixon).inserted_id

print(" Inserted student record Dixon Steele into students collection with document_ID " + str(dixon_student_id))

input("\n\n  End of program, press any key to exit... ")
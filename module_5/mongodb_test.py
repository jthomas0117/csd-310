# Jennifer Thomas - 06/17/21 - CSD 310 - Module 5.2.
# Test to see students collection in pytech database  

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.bjm7n.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print("\n -- Pytech COllection List --")
print(db.list_collection_names())

input("\n\n  End of program, press any key to exit... ")

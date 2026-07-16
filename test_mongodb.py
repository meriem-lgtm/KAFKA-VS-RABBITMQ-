from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["streaming_db"]

collection = db["test"]

collection.insert_one({"message": "MongoDB works!"})

print("Insertion réussie")
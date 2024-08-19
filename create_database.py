from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb+srv://yeauser:yeayea123@testdatabase.tk9k1dw.mongodb.net/yea_database')
# Select the database
db = client.yea_database

# Drop existing collections if they exist
db.user.drop()
db.group.drop()
db.juryvotes.drop()
db.category.drop()

# Create collections
user_collection = db.user
group_collection = db.group
juryvotes_collection = db.juryvotes
category_collection = db.category


from pymongo import MongoClient
from bson.objectid import ObjectId
from create_database import category_collection, user_collection, group_collection
from faker import Faker

# Connect to MongoDB
client = MongoClient('mongodb+srv://yeauser:yeayea123@testdatabase.tk9k1dw.mongodb.net/')

# Select the database
db = client.yea_database
category1 = {"categoryName": "Category 1", "short_id" : "1"}
category2 = {"categoryName": "Category 2", "short_id" : "2"}
category1_id = category_collection.insert_one(category1).inserted_id
category2_id = category_collection.insert_one(category2).inserted_id



groups = [
    { "category": 1, "name": "Marketing Experts", "description": "Group for marketing professionals", "short_id": "0", "points" : 0},
    { "category": 2, "name": "Sales Gurus", "description": "Group for sales professionals", "short_id": "1", "points" : 0},
    { "category": 1, "name": "Tech Innovators", "description": "Group for technology innovators", "short_id": "2", "points" : 0},
    { "category": 2, "name": "Finance Leaders", "description": "Group for finance professionals", "short_id": "3", "points" : 0},
    { "category": 1, "name": "HR Champions", "description": "Group for HR professionals", "short_id": "4", "points" : 0},
    { "category": 2, "name": "Legal Advisors", "description": "Group for legal advisors", "short_id": "5", "points" : 0},
    { "category": 1, "name": "Product Managers", "description": "Group for product managers", "short_id": "6", "points" : 0},
    { "category": 2, "name": "Customer Support Heroes", "description": "Group for customer support professionals", "short_id": "7", "points" : 0},
    { "category": 1, "name": "Project Managers", "description": "Group for project managers", "short_id": "8", "points" : 0},
    { "category": 2, "name": "Design Thinkers", "description": "Group for designers", "short_id": "9", "points" : 0}
]
fake = Faker()
users = [
    # Admins (category 0)
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "Admin", "password": fake.password(), "email": fake.email(), "category": 0 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "Admin", "password": fake.password(), "email": fake.email(), "category": 0 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "Admin", "password": fake.password(), "email": fake.email(), "category": 0 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "Admin", "password": fake.password(), "email": fake.email(), "category": 0 },

    # Users (category 1)
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 1 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 1 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 1 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 1 },

    # Users (category 2)
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 2 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 2 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 2 },
    { "firstName": fake.first_name(), "lastName": fake.last_name(), "role": "User", "password": fake.password(), "email": fake.email(), "category": 2 }
]

# Insert the documents into the collection
result = user_collection.insert_many(users)

# Insert the documents into the collection
result = group_collection.insert_many(groups)

# Print the IDs of the inserted documents
print("Inserted IDs:", result.inserted_ids)

print("Mock data inserted successfully.")
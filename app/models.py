from app import mongo

def get_user_collection():
    return mongo.db.user

def get_category_collection():
    return mongo.db.category

def get_group_collection():
    return mongo.db.group

def get_field_collection():
    return mongo.db.field

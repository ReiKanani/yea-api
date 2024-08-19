from bson import ObjectId

from app.models import get_user_collection, get_group_collection, get_category_collection, get_field_collection


def get_users(filter):
    users_collection = get_user_collection()
    users = users_collection.find()
    users_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        if filter:
            save = True
            for arg in filter:
                if arg[0] not in user or user[arg[0]] != arg[1]:
                    save = False
            if save:
                users_list.append(user)
        else:
            users_list.append(user)

    return users_list

def insert_user(data):
    users_collection = get_user_collection()
    if len(get_users([["firstname", data["firstName"]], ["lastname", data["lastName"]]])) > 0:
        return {"User already exists": "Error"}
    else:
        users_collection.insert_one(data)
        return {"User added successfully" : "Success"}

def update_user(id, data):
    users_collections = get_user_collection()
    result = users_collections.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count > 0:
        return {"User updated successfully": "Success"}
    else:
        return {"User not found": "Error"}


def delete_user(user_id):
    users_collections = get_user_collection()
    result = users_collections.delete_one({'_id': ObjectId(user_id)})

    if result.deleted_count > 0:
        return {"message": "User deleted successfully!"}, 200
    else:
        return {"message": "User not found."}, 404

def authenticate_app(key, id):
    if key == "72176999796131209940" and id == "64494613495769982023":
        return True
    else:
        return False

# Group functions

def get_groups(filter):
    groups_collection = get_group_collection()
    groups = groups_collection.find()
    groups_list = []
    for group in groups:
        group['_id'] = str(group['_id'])
        if filter:
            save = True
            for arg in filter:
                if arg[0] not in group or group[arg[0]] != arg[1]:
                    save = False
            if save:
                groups_list.append(group)
        else:
            groups_list.append(group)

    return groups_list

def insert_group(data):
    groups_collection = get_group_collection()
    if len(get_groups([["name", data["name"]], ["description", data["description"]]])) > 0:
        return {"Group already exists": "Error"}
    else:
        i = 0
        while len(get_groups([["short_id", f"{i}"]])) > 0:
            i += 1
        data["short_id"] = f"{i}"
        groups_collection.insert_one(data)
        return {"Group added successfully" : "Success"}

def update_group(id, data):
    groups_collections = get_group_collection()
    result = groups_collections.update_one({'short_id': id}, {"$set": data})
    if result.matched_count > 0:
        return {"Group updated successfully": "Success"}
    else:
        return {"Group not found": "Error"}


def delete_group(group_id):
    group_collections = get_group_collection()
    result = group_collections.delete_one({'short_id': group_id})

    if result.deleted_count > 0:
        return {"message": "User deleted successfully!"}, 200
    else:
        return {"message": "User not found."}, 404

# Category functions

def get_categories(filter):
    categories_collection = get_category_collection()
    categories = categories_collection.find()
    categories_list = []
    for category in categories:
        category['_id'] = str(category['_id'])
        if filter:
            save = True
            for arg in filter:
                if arg[0] not in category or category[arg[0]] != arg[1]:
                    save = False
            if save:
                categories_list.append(category)
        else:
            categories_list.append(category)

    return categories_list

def insert_category(data):
    categories_collection = get_category_collection()
    if len(get_categories([["name", data["categoryName"]]])) > 0:
        return {"Category already exists": "Error"}
    else:
        i = 0
        while len(get_categories([["short_id" , f"{i}"]])) > 0:
            i+=1
        data["short_id"] = f"{i}"
        categories_collection.insert_one(data)
        return {"Category added successfully" : "Success"}

def update_category(id, data):
    categories_collections = get_category_collection()
    result = categories_collections.update_one({"short_id": id}, {"$set": data})
    if result.matched_count > 0:
        return {"Category updated successfully": "Success"}
    else:
        return {"Category not found": "Error"}

def delete_category(category_id):
    category_collections = get_category_collection()
    result = category_collections.delete_one({"short_id": category_id})

    if result.deleted_count > 0:
        return {"message": "User deleted successfully!"}, 200
    else:
        return {"message": "User not found."}, 404


def add_points(group_id, points):
    if points >= 0:
        if len(get_groups([['short_id', str(group_id)]])) > 0:
            data = get_groups([['short_id', str(group_id)]])[0]
            group_id = data["short_id"]
            data.pop("_id")
            if "points" in data:
                data["points"] += points
            else:
                data["points"] = points
            update_group(group_id, data)
            return {"message": "Points added successfully"}
        else:
            return {"message": f"Group not found {group_id}"}
    else:
        return {"message": "False number of points (n >= 0)"}


def remove_points(group_id, points):
    if points >= 0:
        if len(get_groups([['short_id', str(group_id)]])) > 0:
            data = get_groups([['short_id', str(group_id)]])[0]
            group_id = data["_id"]
            data.pop("_id")
            if "points" in data:
                data["points"] -= points
                if data["points"] < 0:
                    data["points"] = 0
            else:
                data["points"] = 0
            update_group(group_id, data)
            return {"message": "Points removed successfully"}
        else:
            return {"message": f"Group not found {group_id}"}
    else:
        return {"message": "False number of points (n >= 0)"}

def get_field(filter):
    field_collection = get_field_collection()
    fields = field_collection.find()
    field_list = []
    for field in fields:
        field['_id'] = str(field['_id'])
        if filter:
            save = True
            for arg in filter:
                if arg[0] not in field or field[arg[0]] != arg[1]:
                    save = False
            if save:
                field_list.append(field)
        else:
            field_list.append(field)

    return field_list


def delete_field(id):
    field_collections = get_field_collection()
    result = field_collections.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
         return {"message": "User deleted successfully!"}, 200
    else:
        return {"message": "User not found."}, 404

def insert_field(data):
    field_collection = get_field_collection()
    if len(get_field([["fieldName", data["fieldName"]], ["category", data["category"]]])) > 0:
        return {"Group already exists": "Error"}
    else:
        field_collection.insert_one(data)
        return {"Group added successfully": "Success"}
    
def update_field(id, data):
    field_collections = get_field_collection()
    result = field_collections.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count > 0:
        return {"Group updated successfully": "Success"}
    else:
        return {"Group not found": "Error"}

def get_groups_organized(category):
    return sorted(get_groups(filter=[["category", category]]), key=lambda x: x["points"], reverse=True)

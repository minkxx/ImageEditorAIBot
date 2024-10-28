from ImageBot import users_ids_collection


def add_user_to_db(user_id):
    obj_doc = {"users": {"$exists": True}}
    obj = users_ids_collection.find_one(obj_doc)
    if obj:
        data = obj["users"]
        if not user_id in data:
            data.append(user_id)
            update_query = {"$set": {"users": data}}
            users_ids_collection.update_one(obj_doc, update_query)
    else:
        users_ids_collection.insert_one({"users": [user_id]})

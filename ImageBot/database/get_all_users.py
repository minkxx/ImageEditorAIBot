from ImageBot import users_ids_collection

def get_users_from_db():
    obj_doc = {"users": {"$exists":True}}
    obj = users_ids_collection.find_one(obj_doc)
    if obj:
        data = obj["users"]
        return data
    else:
        return []

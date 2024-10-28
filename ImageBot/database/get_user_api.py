from ImageBot import users_api_collection


def get_user_api(user_id):
    user_id = str(user_id)
    obj_doc = {user_id: {"$exists": True}}
    obj = users_api_collection.find_one(obj_doc)
    if not obj:
        return False
    else:
        return obj[user_id]

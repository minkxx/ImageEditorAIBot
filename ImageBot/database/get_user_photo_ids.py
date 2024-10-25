from ImageBot import users_photo_ids_collection

def get_user_photo_id(user_id):
    user_id = str(user_id)
    obj_doc = {user_id: {"$exists":True}}
    obj = users_photo_ids_collection.find_one(obj_doc)
    if not obj:
        return []
    else:
        return obj[user_id]
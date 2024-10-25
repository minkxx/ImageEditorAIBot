from ImageBot import users_photo_ids_collection

def add_user_photo_id(user_id, photo_id):
    user_id = str(user_id)
    obj_doc = {user_id: {"$exists":True}}
    obj = users_photo_ids_collection.find_one(obj_doc)
    if obj:
        data = obj[user_id]
        if not photo_id in data:
            data.append(photo_id)
            update_query = {"$set": {user_id:data}}
            users_photo_ids_collection.update_one(obj_doc, update_query)
    else:
        users_photo_ids_collection.insert_one({user_id:[photo_id]})
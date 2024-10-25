from ImageBot import users_photo_ids_collection
from ImageBot.database.get_user_photo_ids import get_user_photo_id

def delete_user_photo_id(user_id, image_photo_id):
    user_id = str(user_id)
    if image_photo_id in get_user_photo_id(user_id):
        obj_doc = {user_id: {"$exists":True}}
        obj = users_photo_ids_collection.find_one(obj_doc)
        data = obj[user_id]
        data.remove(image_photo_id)
        update_query = {"$set": {user_id:data}}
        users_photo_ids_collection.update_one(obj_doc, update_query)
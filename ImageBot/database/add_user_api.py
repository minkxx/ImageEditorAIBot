from ImageBot import users_api_collection


def add_user_api(
    user_id,
    user_fullname,
    user_cloudinary_cloud_name,
    user_cloudinary_api_key,
    user_cloudinary_api_secret,
):
    user_id = str(user_id)
    obj_doc = {user_id: {"$exists": True}}
    obj = users_api_collection.find_one(obj_doc)
    if obj:
        return {"status": "user have already added api!"}
    else:
        data = {
            "user_id": user_id,
            "user_fullname": user_fullname,
            "cloud_name": user_cloudinary_cloud_name,
            "api_key": user_cloudinary_api_key,
            "api_secret": user_cloudinary_api_secret,
        }
        users_api_collection.insert_one({user_id: data})
        return {"status": "user api added succesfully"}

from ImageBot.database.get_user_api import get_user_api

from ImageBot.services.cloudinary.cloudinary import CloudinaryAPI


def load_api_client(user_id):
    data = get_user_api(user_id)
    api_cli = CloudinaryAPI(
        cloud_name=data["cloud_name"],
        api_key=data["api_key"],
        api_secret=data["api_secret"],
    )
    return api_cli

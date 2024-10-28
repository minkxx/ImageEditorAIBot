from ImageBot.services.cloudinary.load_client import load_api_client


def get_user_photo_id(user_id):
    api_cli = load_api_client(user_id)
    return api_cli.get_photo_ids()

from pymongo.mongo_client import MongoClient

from ImageBot import MONGO_DB_URI


def get_connection():
    try:
        return MongoClient(MONGO_DB_URI)
    except Exception as e:
        print("Unable to connect to database...")
        print(e)
        exit()

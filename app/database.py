# Utils
from decouple import config

# MongoDB
from pymongo import MongoClient


client = MongoClient(config('MONGODB_URL'))

database = client.marvel_comics
users_collection = database.users

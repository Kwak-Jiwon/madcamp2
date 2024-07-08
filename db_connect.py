from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jw101102:8tzDsS1NO1GNKCKT@barybary.xjpidiu.mongodb.net/?appName=barybary"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['dkandlfma']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
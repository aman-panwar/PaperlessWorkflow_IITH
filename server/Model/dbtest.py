from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv:// : @cluster0.iz8c5af.mongodb.net/?retryWrites=true&w=majority")
    print('connected successfully')
except Exception as e:
    print(e)

try:
    db = client.get_database('sample_airbnb')
    print('db accessed')
    print(db)
except Exception as e:
    print(e)
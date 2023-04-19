from pymongo import MongoClient

host = 'mongodb+srv://cs20btech11004:Y1JDdwqWBLgOWp2g@cluster0.iz8c5af.mongodb.net/?retryWrites=true&w=majority'

try:
    client = MongoClient(host)
    print('connected successfully')
except Exception as e:
    print('eroor')

try:
    db = client.get_database('PaperlessWorkflow')


except Exception as e:
    print('errro 2')



# my_dict = {
#     "_id": '643ff5dd326f4d6638bea447',
#     "type": "leave",
#     "form_data": "lmao help me"
# }

c = db.get_collection('Forms')
# c.insert_one(my_dict)
# print('yeee')

for x in c.find({"_id":"643ff5dd326f4d6638bea447"}):
    print(x)
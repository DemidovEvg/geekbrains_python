import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client['vacancy_database']

for col_name in db.list_collection_names():
    db.drop_collection(col_name)

print(db.list_collection_names())
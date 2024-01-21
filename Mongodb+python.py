import pymongo
from pymongo import MongoClient

# Replace 'your_mongodb_uri' with your MongoDB URI (e.g., 'mongodb://localhost:27017/')
client = MongoClient('mongodb://localhost:27017/')
db = client['School']
collection = db['Student_Info']

# - Create (Insert): python
data_to_insert = {
    "name": "shaheer",
    "roll#": "19011598-124",
    # Add more fields as needed
}
# Insert a single document
inserted_doc = collection.insert_one(data_to_insert)

# - Read (Query):python

# Find a single document
query = {"name": "shaheer"}
result = collection.find_one(query)

# Find all documents matching a query
query = {"roll#": "19011598-124"}
results = collection.find(query)

# Print the results
for doc in results:
    print(doc)

# - Update:python
# Update a single document
query = {"name": "shaheer"}
new_values = {"$set": {"roll#": "19011598-123"}}
collection.update_one(query, new_values)


# - Delete:python
# Delete a single document
query = {"name": "shaheer"}
# collection.delete_one(query)

# Delete all documents matching a query
query = {"roll#": "19011598-124"}
# collection.delete_many(query)

client.close()


from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId



class MongoDBConnectionManager:

    HOST_ADDRESS = "mongodb://localhost:27017/"


    def __init__(self, database: str, collection: str) -> None:
        self.client = MongoClient(self.HOST_ADDRESS)
        self.database = self.client[database]
        self.collection = self.database[collection]


    def set_index(self, index_name):

        indexes = self.collection.list_indexes()
        for index in indexes:
            if index["name"] == index_name:
                return 
            
        index_to_set = (f"{index_name}", 1)
        self.collection.create_index(keys=[index_to_set,], expireAfterSeconds=0)


    def find_data_by_id(self, instance_id: ObjectId):
        result = self.collection.find_one({"_id":instance_id})
        if result:
            result["_id"] = str(result["_id"])
        return result


    def find_data_by_another_field(self, field_name: str, field_data: str):
        result = self.collection.find_one({f"{field_name}":field_data})
        return result
    

    def save_data_to_db_collection(self, instance: BaseModel):
        result = self.collection.insert_one(instance)
        return result


    def get_data_from_db_collection(self):
        data_list = list()

        collection_datas = self.collection.find()

        for data in collection_datas:
            data["_id"] = str(data["_id"])
            data_list.append(data)

        return data_list


    def delete_data_from_db_collection(self, instance_id: ObjectId):
        result = self.collection.find_one_and_delete({"_id":instance_id})
        return result


    def update_db_collection_data(self, instance_id: ObjectId, updated_instance: BaseModel):
        result = self.collection.update_one({"_id": instance_id}, {"$set": updated_instance})
        return result
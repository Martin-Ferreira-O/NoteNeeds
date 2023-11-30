from pymongo import MongoClient
from pymongo.database import Database

URI = ""

class Database:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = client["users"]

    def create_profile(self, name, rut, university):

        profile = self.db["profile"] # Select the "usuarios" collection from the database
        _id = profile.count_documents({}) + 1

        profile_default = {
            "_id": _id,
            "name": name,
            "rut": rut,
            "universidad": university
        }

        profile.insert_one(profile_default)


    def add_course(self, course: dict):
        # course need _id, name, grade[]
        # grade: {grade, weight}
        try:
            self.db["course"].insert_one(course)
        except Exception as e:
            print(e)


    def add_grade(self, course_id: int, grade: dict):
        
        try:
            self.db["course"].find_one_and_update(
                {"_id": course_id},
                {"$push": {"grade": grade}}
            )
        except Exception as e:
            print(e)

    def get_profile(self ,_id: int):
        return self.db["profile"].find_one({"_id": _id})

    def get_course(self, _id: int):
        return self.db["course"].find_one({"_id": _id})


#db = connect()
#create_profile(db, "ALVARO", "123456789", "UA")
#create_profile(db, "jaz", "123456789", "UA")


#add_course(db)
# Agregar Nota
#dd_grade(db, 1, {
#     "grade": 5,
#    "weight": 0.3
#})

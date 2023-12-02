from pymongo import MongoClient
from pymongo.database import Database

URI = ""

# _id deberia ser el rut, ya que es un identificador unico
# No utilizar un id incremental, ya que si se borra un perfil, se pierde el orden

class Database:
    def __init__(self):
        self.client = MongoClient(URI)
        self.db = self.client["users"]

    def create_profile(self, name, rut, university):

        profile = self.db["profile"] # Select the "usuarios" collection from the database

        profile_default = {
            "_id": rut,
            "name": name,
            "universidad": university
        }

        profile.insert_one(profile_default)


    # El _id del curso, no puede ser el rut del estudiante, ya que un estudiante puede tener varios cursos
    # por lo que el _id deberia ser un identificador unico del curso

    def add_course(self, course: dict):
        course_default = {
            "_id": 1,
            "name": "Calculo 1",
            "grade": [
                {"grade": 5, "weight": 0.3},
                {"grade": 4, "weight": 0.3},
                {"grade": 3, "weight": 0.4}
            ]
        }
        
        # Creame un metodo que permita establecer un _id para el curso
        try:
            self.db["course"].insert_one(course_default)
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

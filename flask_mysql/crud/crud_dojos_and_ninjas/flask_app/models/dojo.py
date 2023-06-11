from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.ninja import Ninja

DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.name}"
    

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        dojo = Dojo (result[0])
        print(dojo.ninjas)
        for row_from_db in result:
            temp_ninja = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at'],
                'dojo_id' : row_from_db['dojo_id']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for u in results:
            dojos.append( cls(u) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        # comes back as the new row id
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
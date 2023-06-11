from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint
DATABASE = 'belt'

class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO paintings (title, description, price, quantity, user_id) VALUES (%(title)s, %(description)s, %(price)s, %(quantity)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s, quantity = %(quantity)s WHERE paintings.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM paintings JOIN users ON users.id = paintings.user_id WHERE paintings.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        return Painting(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paintings JOIN users ON users.id = paintings.user_id"
        results = connectToMySQL(DATABASE).query_db(query)
        paintings = []
        for painting in results:
            paintings.append(cls(painting))
        return paintings

    @staticmethod
    def validate_painting(painting:dict) -> bool:
        is_valid = True
        if len(painting['title']) < 2:
            flash("title must be 2 characters")
            is_valid = False
        if len(painting['description']) < 10:
            flash("description must be 10 characters")
            is_valid = False
        if int(painting['price']) < 0:
            flash('Price must be greater than $0.')
            is_valid = False
        if int(painting['quantity']) < 0:
            flash('Quantity must be greater than $0.')
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
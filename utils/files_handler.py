import json
from models import Book, User 

def load_data(filepath , cls):
    try:
        with open(filepath , 'r') as file: 
            data = json.load(file)
            result = {}
            for dict in data: 
                obj = cls(dict)
                result[obj.getId()] = obj
            return result
    except FileNotFoundError:
        print("File is missing!")
        return []
    except Exception as e:
        print(f"An unexpected error occurred! The message is: {e}")
        return []
        
def save_data(data , filepath):
    try:
        with open(filepath , "w") as file:
            json.dump(data , file , indent = 4)
    except Exception as e:
        print(f"An unexpected error occurred! The message is: {e}")
    
def initialize_system():
    books_data = load_data("data/books.json", Book)
    user_data = load_data("data/users.json" , User)
    







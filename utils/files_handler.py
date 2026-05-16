import json
import models 

def load_data(filepath):
    try:
        with open(filepath , 'r') as file: 
            return json.load(file)
    except FileNotFoundError:
        print("File is missing!")
        return []
    except Exception as e:
        print(f"An unexpected error occurred! The message is: {e}")
        return []
        
books = load_data("data/books.json")
users = load_data("data/books.json")

def save_data(data , filepath):
    try:
        with open(filepath , "w") as file:
            json.dump(data , file , indent = 4)
    except Exception as e:
        print(f"An unexpected error occurred! The message is: {e}")
    





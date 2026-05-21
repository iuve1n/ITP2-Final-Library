import json
from models.book import Book
from models.user import User


def load_data(filepath, cls):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            result = {}
            for item in data:
                obj = cls(item)
                result[obj.get_id()] = obj
            return result
    except FileNotFoundError:
        print("File is missing!")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred! The message is: {e}")
        return {}


def save_data(filepath, data):
    try:
        output = []
        if isinstance(data, dict):
            for item in data.values():
                if hasattr(item, "to_dict"):
                    output.append(item.to_dict())
                else:
                    output.append(item)
        else:
            output = data

        with open(filepath, "w", encoding='utf-8') as file:
            json.dump(output, file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred! The message is: {e}")


def initialize_system():
    books_data = load_data("data/books.json", Book)
    users_data = load_data("data/users.json", User)
    return books_data, users_data







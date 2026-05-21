class Person:
    def __init__(self,dict):
        self.user_id= int(dict["user_id"])
        self.name= dict["name"]
    def get_id(self):
        return self.user_id
    def get_role(self):
        return"Person"
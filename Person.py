import json
import os
from os.path import join
class Person:

    def __init__(self):
        self.data = {
            "name" : str,
            "pic_path" : str,
            "Age" : int
        }
        os.makedirs("user_data", exist_ok=True)   
    def register(self, name, age, pic_path):
        
        self.data = {
            "name" : name,
            "pic_path" : pic_path,
            "Age" : age
        }
        file_name = self.data["name"]
        with open(join("./Auth", f"{file_name}.json"), "w") as f:
            json.dump(self.data, f)


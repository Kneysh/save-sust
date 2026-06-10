import json


class Highest_Time():
    def __init__(self):
        self.path = "highest_time.json"

    def load_highest(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                return data.get("highestTime", 0)
            
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
        
    def save_highest(self, highestTime):
        data = {
            "highestTime" : highestTime
        }

        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
        



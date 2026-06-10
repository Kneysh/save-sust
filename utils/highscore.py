import json


class High_Score():
    def __init__(self):
        self.path = "high_score.json"

    def load_highest(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                return data.get("highScore", 0)
            
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
        
    def save_highest(self, highScore):
        data = {
            "highScore" : highScore
        }

        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
        



import requests

parameters = {"amount": 10,
              "type": "boolean",
              "difficulty": "easy",
              "category": 18}

r = requests.get("https://opentdb.com/api.php?", params=parameters)
data = r.json()
question_data = data["results"]

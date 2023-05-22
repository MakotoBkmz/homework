import requests
url = "https://dummyjson.com/users?limit=100"
response = requests.get(url)
data = response.json()

louisville_citizen = [user for user in data["users"] if user["address"].get("city", '') == "Louisville"]
men_with_brown_hair = [user["age"] for user in data["users"] if user["gender"] == "male" and user["hair"]["color"] == "Brown"]
if men_with_brown_hair:
    average_age_men_with_brown_hair = sum(men_with_brown_hair) / len(men_with_brown_hair)
    print("Средний возраст мужчин с коричневыми волосами:", average_age_men_with_brown_hair)
print("Список мужчин с коричневыми волосами в городе Louisville:")
for person in louisville_citizen:
    print(person["firstName"], person["lastName"])


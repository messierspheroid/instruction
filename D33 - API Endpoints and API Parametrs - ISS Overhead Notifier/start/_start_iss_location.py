import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# status codes; 1XX: hold on, 2XX: request received, 3XX: go away, 4XX: you screwed up, 5XX: I screwed up
# print(response.status_code)
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(data)

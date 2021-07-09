import requests
from datetime import datetime

MY_LAT = 37.774929
MY_LNG = -122.419418

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# some api sites give sample requests; https://"api endpoint" + ? + "param name" + "=" + "&" ...
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunrise = data["results"]["sunrise"] = 2021-02-25T14:45:01+00:00
# sunrise = data["results"]["sunrise"].split("T") = '2021-02-25', '14:45:01+00:00'
# sunrise = data["results"]["sunrise"].split("T")[1] = 14:45:01+00:00
# sunrise = data["results"]["sunrise"].split("T")[1].split(":") = '14', '45', '01+00', '00'
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] = 14
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now().hour
print(time_now)

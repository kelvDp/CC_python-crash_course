import requests
import json

appID= "48627f8b32f9b8d0b13d455bbf3c6f37"
url = "http://api.openweathermap.org/data/2.5/weather?q=Johannesburg&appid="+appID+"&units=metric"

r = requests.get(url)

response = r.json()

# with open("file.json","w") as f:
#     json.dump(response,f, indent=4)

print(f"Status_code: {response['cod']}")
print(f"Here is the weather info for {response['name']} :\n")
print(f"The current high is {response['main']['temp_max']} degrees celsius.\nThe current low is {response['main']['temp_min']} degrees celsius")
    
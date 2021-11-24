import requests

url = "https://shazam.p.rapidapi.com/auto-complete"

querystring = {"term":"hands up","locale":"en-US"}

headers = {
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
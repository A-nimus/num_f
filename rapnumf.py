import requests

num = int(input('ENTER YOUR FAVOURITE WHOLE NUMBER: '))

url = (f"https://numbersapi.p.rapidapi.com/{num}/math")

querystring = {"fragment":"true","json":"true"}

headers = {
    'x-rapidapi-key': "90be0bff7fmsh2bc48323db706d5p1e5386jsn889518c00238",
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

txt = response.json()
n='\n'
print(f"{n}Fact related to {num} :{n}{n}{num} is {txt['text']}")

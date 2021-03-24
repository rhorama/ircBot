import requests
import json
import xmltodict
from os import getenv
from dotenv import load_dotenv

load_dotenv()
userInput = "9*9"
appid = getenv('APIKEY_WOLFRAMALPHA')
url = f"http://api.wolframalpha.com/v2/query?input={userInput}&appid="
response = xmltodict.parse(requests.get(url).content)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

jres = jprint(response)
print(jres)
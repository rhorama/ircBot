import requests
import json
import xmltodict

userInput = "9*9"
appname = "rhobotIRCbot"
appid = "&appid=72VHA3-PGATP7T5KH"
url = "http://api.wolframalpha.com/v2/query?input=" + userInput + appid
response = xmltodict.parse(requests.get(url).content)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

jres = jprint(response)
print(jres)
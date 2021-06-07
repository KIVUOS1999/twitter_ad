import requests
import json
URL = "http://127.0.0.1:8000/data/"

data = {
    'api_key' : 'BoIvbhijJCmXTv8ig6gdZmxhM',
    'api_secreat_key' : 'vEis1bILMeFOTuV1bnwMhv5PxD5T3fF6ERYpNHuR1t4RKDjEa0',
    'access_token' : '1400422259051823105-05StBhNmMzcThLPkjDYmyOl7dtzzPc',
    'access_token_secreat' : 'xO52LRZGP2DZJRd1gjfyEQA2VADTJaQxQoaf9CWPFfnXG',
    'hashtag' : '#Army',
    'numbers' : 10,
    'comment' : 'Proud of you'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
try:
    data = r.json()
except:
    data = ("Server error")

print(data)
import base64
import json

import requests,time



session = requests.Session()

url = f"https://www.dianxiaomi.com/verify/code.htm?t={int(time.time()*1000)}"

response = session.get(url)

img_base64 = base64.b64encode(response.content).decode()

url2 = 'https://api.cyymzy.com/items/img_base64'

data = {
    'img_base64': img_base64
}

response2 = session.post(url2, data=json.dumps(data))

print(response2.json()['message'])
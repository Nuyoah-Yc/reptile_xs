import requests,re

url = 'https://www.dianxiaomi.com/crawl/list.htm'
headers = {
    'Cookie': 'Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1716378074; _dxm_ad_client_id=A166A34BC8B6DDD9E2F8DB07B91C19FE7; dxm_i=MTYxNDQ1NSFhVDB4TmpFME5EVTEhOGZmMjc3ZmM5YWJhOGU4ZDUwZjg5ODJiNzg3NGQ5ZDQ; dxm_t=MTcxNjQzMzIxMiFkRDB4TnpFMk5ETXpNakV5ITRiZTg2Njk3OGM5YzdjNTc5YTRhOTQ4MGNjMTM1OWRj; dxm_c=YzZVWXJMd1QhWXoxak5sVlpja3gzVkEhOTk5Y2NjOTAxOGZkYzJhYzMyNWRlYTI3ZWM4Zjc3MjU; dxm_w=ZDEwYTcwMTA5Yzg2YTM2ZTgwMzJmZWRkYWFiOWFmYjchZHoxa01UQmhOekF4TURsak9EWmhNelpsT0RBek1tWmxaR1JoWVdJNVlXWmlOdyE3N2M1OWYzYTk5YWFkMmVjMzg3YjhmOTdhOWFkYTQxNg; dxm_s=rav-G5sVoKDLJtw3LWk6GgWHV_Qrlb0ch38bNzGvEk8; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1716434237; JSESSIONID=E375001AC562A4A7C804FE72F66850B9',
    'Origin': 'https://www.dianxiaomi.com',
    'Referer': 'https://www.dianxiaomi.com/crawl/index.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

data = {
    'pageNo': 1,
    'pageSize': 300,
    'state': 'no',
    'site': 'all',
    'searchValue': '',
    'productSearchType': 'name',
    'sortTime': '',
    'accountName': '',
    'commentType': '',
    'commentValue': '',
}

response = requests.post(url, headers=headers, data=data)

print(response.text)

url_list = re.findall('<a href="//(.*?)" target="_blank">编辑</a>', response.text)
print(url_list)
print(len(url_list))
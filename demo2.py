import requests
import re
from lxml import html

url = 'https://www.dianxiaomi.com/tiktokProduct/pageList.htm'
headers = {
    'Cookie': 'Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1716378074; _dxm_ad_client_id=A166A34BC8B6DDD9E2F8DB07B91C19FE7; dxm_i=MTYxNDQ1NSFhVDB4TmpFME5EVTEhOGZmMjc3ZmM5YWJhOGU4ZDUwZjg5ODJiNzg3NGQ5ZDQ; dxm_t=MTcxNjQzMzIxMiFkRDB4TnpFMk5ETXpNakV5ITRiZTg2Njk3OGM5YzdjNTc5YTRhOTQ4MGNjMTM1OWRj; dxm_c=YzZVWXJMd1QhWXoxak5sVlpja3gzVkEhOTk5Y2NjOTAxOGZkYzJhYzMyNWRlYTI3ZWM4Zjc3MjU; dxm_w=ZDEwYTcwMTA5Yzg2YTM2ZTgwMzJmZWRkYWFiOWFmYjchZHoxa01UQmhOekF4TURsak9EWmhNelpsT0RBek1tWmxaR1JoWVdJNVlXWmlOdyE3N2M1OWYzYTk5YWFkMmVjMzg3YjhmOTdhOWFkYTQxNg; dxm_s=rav-G5sVoKDLJtw3LWk6GgWHV_Qrlb0ch38bNzGvEk8; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1716434237; JSESSIONID=E375001AC562A4A7C804FE72F66850B9',
    # 'Origin': 'https://www.dianxiaomi.com',
    # 'Referer': 'https://www.dianxiaomi.com/crawl/index.htm',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

data = {
    "shopGroupId": "",
    "pageNo": 1,
    "pageSize": 1000,
    "shopId": -1,
    "searchType": 2,
    "searchValue": "",
    "sortName": 2,
    "sortValue": 0,
    "dxmState": "draft",
    "dxmOfflineState": "",
    "productSearchType": 1,
    "fullCid": "",
    "productStatus": "",
    "advancedSearch": "",
    "priceLift": "",
    "priceRight": "",
    "quantityLift": "",
    "quantityRight": "",
    "isGlobalWarehouse": "",
    "weightLeft": "",
    "weightRight": "",
    "categoryId": "",
    "warrantyPeriod": "",
    "sourceUrl": "",
    "commentType": 0,
    "commentContent": "",
    "advancedTime": 1,
    "timeLift": "",
    "timeRight": "",
    "warehouseId": ""
}

response = requests.post(url, headers=headers, data=data)

# print(response.text)
html_text = html.fromstring(response.text)

def extract_number(text):
    match = re.search(r'[\d.]+', text)
    return match.group() if match else None

id_list = re.findall('"tiktok" data-id="(.*?)"', response.text)
img_list = re.findall('data-original="(.*?)" referrerpolicy="', response.text)
gbp_list = html_text.xpath('//*[@id="goodsContent"]/table/tbody/tr/td/table//tr[1]/td[2]/text()')
numbers = [extract_number(text) for text in gbp_list if extract_number(text) is not None]

# 确保所有列表长度一致
min_length = min(len(id_list), len(img_list), len(numbers))
id_list = id_list[:min_length]
img_list = img_list[:min_length]
numbers = numbers[:min_length]

# 封装成列表套字典
result_list = [{"id": id, "img": img, "number": number} for id, img, number in zip(id_list, img_list, numbers)]

print(result_list)
print(len(result_list))

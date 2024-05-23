import requests,pandas as pd
from lxml import html

url = 'https://www.dianxiaomi.com/tiktokProduct/edit.htm?id=110345269926896906'
headers = {
    'Cookie': 'Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1716378074; _dxm_ad_client_id=A166A34BC8B6DDD9E2F8DB07B91C19FE7; dxm_i=MTYxNDQ1NSFhVDB4TmpFME5EVTEhOGZmMjc3ZmM5YWJhOGU4ZDUwZjg5ODJiNzg3NGQ5ZDQ; dxm_t=MTcxNjQzMzIxMiFkRDB4TnpFMk5ETXpNakV5ITRiZTg2Njk3OGM5YzdjNTc5YTRhOTQ4MGNjMTM1OWRj; dxm_c=YzZVWXJMd1QhWXoxak5sVlpja3gzVkEhOTk5Y2NjOTAxOGZkYzJhYzMyNWRlYTI3ZWM4Zjc3MjU; dxm_w=ZDEwYTcwMTA5Yzg2YTM2ZTgwMzJmZWRkYWFiOWFmYjchZHoxa01UQmhOekF4TURsak9EWmhNelpsT0RBek1tWmxaR1JoWVdJNVlXWmlOdyE3N2M1OWYzYTk5YWFkMmVjMzg3YjhmOTdhOWFkYTQxNg; dxm_s=rav-G5sVoKDLJtw3LWk6GgWHV_Qrlb0ch38bNzGvEk8; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1716434237; JSESSIONID=E375001AC562A4A7C804FE72F66850B9',
    'Referer': 'https://www.dianxiaomi.com/crawl/edit.htm?id=110345270305925386',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

rsp = requests.get(url, headers=headers)

print(rsp.text)


data_info = {}
data_info['Category'] = 110345270305925386 #产品分类
data_info['Brand'] = None
data_info['Product Name'] = None #产品标题
data_info['Product Description'] = None #产品描述
data_info['Package weight(g)'] = None #重量
data_info['Package length(cm)'] = None #长度
data_info['Package width(cm)'] = None #宽度
data_info['Package height(cm)'] = None #高度
data_info['Delivery options'] = None
data_info['Identifier code type'] = None
data_info['Identifier code'] = None
data_info['Variation 1'] = None #颜色变化1
data_info['Variation 2'] = None #尺寸变化2
data_info['Variant image'] = None #变体图片
data_info['Retail Price (Local Currency)'] = None #价格
data_info['Quantity'] = None #商品库存
data_info['Seller SKU'] = None
data_info['Main Product Image'] = None #主图
data_info['Product Image 2'] = None #副图1
data_info['Product Image 3'] = None #副图2
data_info['Product Image 4'] = None #副图3
data_info['Product Image 5'] = None #副图4
data_info['Product Image 6'] = None #副图5
data_info['Product Image 7'] = None #副图6
data_info['Product Image 8'] = None #副图7
data_info['Product Image 9'] = None #副图8
data_info['Size Chart'] = None
data_info['Warranty Type'] = None
data_info['Battery in The Product'] = None
data_info['Plug Type'] = None
data_info['Storage Capacity'] = None
data_info['Material'] = None
data_info['Model'] = None
data_info['Memory Card Type'] = None
data_info['Battery Type'] = None
data_info['Optical Zoom'] = None
data_info['Maximum Aperture'] = None
data_info['Minimum Aperture'] = None
data_info['Warranty Period'] = "Not Applicable"
data_info['UKCA/CE mark'] = None #UKCA/CE标记
data_info['Product status'] = "Active(1)"


df = pd.DataFrame(data_info, index=[0])  # 转换为DataFrame格式
df.to_csv('demo4.csv', index=False)
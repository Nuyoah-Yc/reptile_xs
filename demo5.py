import requests, json, pandas as pd, re
from lxml import etree, html


def get_html():
    # 定义要爬取的URL
    url = 'https://www.dianxiaomi.com/tiktokProduct/edit.htm?id=110345269926896906'

    # 定义browserless/chrome的API端点
    browserless_url = 'http://192.168.20.159:3000/content'

    # 解析cookie字符串
    cookie_string = "Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1716378074; _dxm_ad_client_id=A166A34BC8B6DDD9E2F8DB07B91C19FE7; dxm_i=MTYxNDQ1NSFhVDB4TmpFME5EVTEhOGZmMjc3ZmM5YWJhOGU4ZDUwZjg5ODJiNzg3NGQ5ZDQ; dxm_t=MTcxNjQzMzIxMiFkRDB4TnpFMk5ETXpNakV5ITRiZTg2Njk3OGM5YzdjNTc5YTRhOTQ4MGNjMTM1OWRj; dxm_c=YzZVWXJMd1QhWXoxak5sVlpja3gzVkEhOTk5Y2NjOTAxOGZkYzJhYzMyNWRlYTI3ZWM4Zjc3MjU; dxm_w=ZDEwYTcwMTA5Yzg2YTM2ZTgwMzJmZWRkYWFiOWFmYjchZHoxa01UQmhOekF4TURsak9EWmhNelpsT0RBek1tWmxaR1JoWVdJNVlXWmlOdyE3N2M1OWYzYTk5YWFkMmVjMzg3YjhmOTdhOWFkYTQxNg; dxm_s=rav-G5sVoKDLJtw3LWk6GgWHV_Qrlb0ch38bNzGvEk8; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1716449026; JSESSIONID=AC81388D44A14E4F5EC5074EBEBDB321"

    # 将cookie字符串解析为列表
    cookies = []
    for cookie in cookie_string.split('; '):
        name, value = cookie.split('=', 1)
        cookies.append({
            "name": name,
            "value": value,
            "domain": ".dianxiaomi.com",
            "path": "/"
        })

    # 定义要发送到browserless/chrome的payload
    payload = {
        "url": url,
        "cookies": cookies,
        "gotoOptions": {
            "timeout": 30000,  # 超时时间设置为30秒
            "waitUntil": "networkidle0"  # 等待网络空闲状态
        }
    }

    # 发送POST请求到browserless/chrome服务
    response = requests.post(browserless_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    # 检查响应状态码
    if response.status_code == 200:
        # 获取渲染后的页面内容
        rendered_html = response.text
        return rendered_html
    else:
        print(f"Failed to fetch page: {response.status_code}")
        print(response.text)  # 输出错误详情


def get_data():
    htmls = etree.HTML(get_html())

    data_info = {}
    data_info['Category'] = re.sub(r'\(.*?\)', '', ''.join(
        htmls.xpath('//span[@class="category productCategory"]/span/span/text()')).replace('\xa0>\xa0', ' > ').strip())
    data_info['Brand'] = None
    data_info['Product Name'] = htmls.xpath('//*[@id="productTitle"]/@value')[0]
    data_info['Product Description'] = f"""
        {html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).text_content()},
        {','.join(html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).xpath('//img/@src'))}
    """
    data_info['Package weight(g)'] = htmls.xpath('//*[@id="proWeight"]/@value')[0]
    data_info['Package length(cm)'] = htmls.xpath('//*[@id="proLength"]/@value')[0]
    data_info['Package width(cm)'] = htmls.xpath('//*[@id="proWidth"]/@value')[0]
    data_info['Package height(cm)'] = htmls.xpath('//*[@id="proHeight"]/@value')[0]
    data_info['Delivery options'] = None
    data_info['Identifier code type'] = None
    data_info['Identifier code'] = None
    data_info['Variation 1'] = '\n\n'.join(
        htmls.xpath('//*[@id="skuInfoArrBox"]/div[1]/div[2]/div[1]/div/label/span/text()'))
    data_info['Variation 2'] = '\n\n'.join(
        htmls.xpath('//*[@id="skuInfoArrBox"]/div[2]/div[2]/div[1]/div/label/span[2]/text()'))
    data_info['Variant image'] = '\n\n'.join(f'({name}:{link})' for name, link in zip(htmls.xpath(
        '//*[@id="skuInfoArrBox"]/div[3]/div[2]/div/div/div[1]/text()'), htmls.xpath(
        '//*[@id="skuInfoArrBox"]/div[3]/div[2]/div/div/div[2]/div[1]/img/@src')))
    data_info['Retail Price (Local Currency)'] = None  # 零售价
    data_info['Quantity'] = 200
    data_info['Seller SKU'] = None
    data_info['Main Product Image'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[0]
    data_info['Product Image 2'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[1]
    data_info['Product Image 3'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[2]
    data_info['Product Image 4'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[3]
    data_info['Product Image 5'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[4]
    data_info['Product Image 6'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[5]
    data_info['Product Image 7'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[6]
    data_info['Product Image 8'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[7]
    data_info['Product Image 9'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[8]
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
    data_info['UKCA/CE mark'] = None
    data_info['Product status'] = "Active(1)"

    df = pd.DataFrame(data_info, index=[0])
    df.to_csv('data.csv', index=False)
    # print(data_info['Product Description'])


get_data()

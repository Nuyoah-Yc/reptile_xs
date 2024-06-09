import itertools

import requests, json, pandas as pd, re
from lxml import etree, html


def get_html():
    url = f"https://www.dianxiaomi.com/tiktokProduct/edit.htm?id=110345269926896906"

    # 定义browserless/chrome的API端点
    browserless_url = 'http://110.40.40.22:3001/chrome/content'

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
    html_text = get_html()
    if not html_text:
        return "没有获取到数据"
    htmls = etree.HTML(html_text)

    data_info = {}
    data_info['Category'] = re.sub(r'\(.*?\)', '', ''.join(
        htmls.xpath('//span[@class="category productCategory"]/span/span/text()')).replace('\xa0>\xa0', ' > ').strip())
    data_info['Brand'] = None
    data_info['Product Name'] = htmls.xpath('//*[@id="productTitle"]/@value')[0]
    # data_info['Product Description'] = f"""
    #     {html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).text_content()},
    #     {','.join(html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).xpath('//img/@src'))}
    # """
    data_info['Product Description'] = html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).text_content()
    data_info['Package weight(g)'] = float(htmls.xpath('//*[@id="proWeight"]/@value')[0]) * 1000
    data_info['Package length(cm)'] = htmls.xpath('//*[@id="proLength"]/@value')[0]
    data_info['Package width(cm)'] = htmls.xpath('//*[@id="proWidth"]/@value')[0]
    data_info['Package height(cm)'] = htmls.xpath('//*[@id="proHeight"]/@value')[0]
    data_info['Delivery options'] = None
    data_info['Identifier code type'] = None
    data_info['Identifier code'] = None
    data_info['Variation 1'] = ','.join(
        htmls.xpath('//*[@id="skuInfoArrBox"]/div/div[2]/div/div/div[1]/text()'))
    data_info['Variation 2'] = ','.join(
        set(htmls.xpath('//*[@id="skuInfoTable"]/tbody/tr/td[2]/text()')))
    data_info['Variant image'] = ','.join(htmls.xpath(
        '//*[@id="skuInfoArrBox"]/div/div[2]/div/div/div[2]/div[1]/img/@src'))
    data_info['Retail Price (Local Currency)'] = None
    data_info['Quantity'] = 200
    data_info['Seller SKU'] = None
    data_info['Main Product Image'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[0]
    data_info['Product Image 2'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[1]
    data_info['Product Image 3'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[2]
    data_info['Product Image 4'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[3]
    data_info['Product Image 5'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[4]
    data_info['Product Image 6'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[5]
    try:
        data_info['Product Image 7'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[6]
    except IndexError:
        data_info['Product Image 7'] = None
    try:
        data_info['Product Image 8'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[7]
    except IndexError:
        data_info['Product Image 8'] = None
    try:
        data_info['Product Image 9'] = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')[8]
    except IndexError:
        data_info['Product Image 9'] = None
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
    print(data_info['Variation 1'])
    # df = pd.DataFrame(data_info, index=[0])
    # # 将需要拆分的列按逗号拆分
    # df['Variation 1'] = df['Variation 1'].str.split(',')
    # df['Variation 2'] = df['Variation 2'].str.split(',')
    # df['Variant image'] = df['Variant image'].str.split(',')
    #
    # # 初始化一个空的DataFrame来存储结果
    # result = pd.DataFrame()
    #
    # # 对每一行进行处理
    # for i, row in df.iterrows():
    #     variations_1 = row['Variation 1']
    #     variations_2 = row['Variation 2']
    #     variant_images = row['Variant image']
    #
    #     # 确保Variation 1和Variant image数量一致，不足则填充为空
    #     max_length = max(len(variations_1), len(variant_images))
    #     variations_1 += [''] * (max_length - len(variations_1))
    #     variant_images += [''] * (max_length - len(variant_images))
    #
    #     # 对Variation 1和Variation 2进行笛卡尔积
    #     product_variations = list(itertools.product(variations_1, variations_2))
    #
    #     # 生成包含Variation 1, Variation 2和Variant image的DataFrame
    #     expanded_rows = pd.DataFrame(product_variations, columns=['Variation 1', 'Variation 2'])
    #
    #     # 确保图片数量与变种名称一致并进行笛卡尔积
    #     expanded_rows['Variant image'] = [variant_images[i // len(variations_2)] for i in range(len(expanded_rows))]
    #
    #     # 将其他列的值重复添加到笛卡尔积中
    #     for col in df.columns:
    #         if col not in ['Variation 1', 'Variation 2', 'Variant image']:
    #             expanded_rows[col] = row[col]
    #
    #     # 将处理后的行添加到结果中
    #     result = pd.concat([result, expanded_rows], ignore_index=True)
    #
    # # 确保列名顺序正确
    # result = result[df.columns]
    #
    # # 重置索引以保持数据整洁
    # result = result.reset_index(drop=True)
    #
    # # 将处理后的数据保存到新文件
    # result.to_csv(f'{id}.csv', index=False)


# a = input("TikTok ID: ")
# b = a.split(",")
# for i in b:
#     get_data(i)
#     print(f"已爬取{i}号商品数据")

get_data()
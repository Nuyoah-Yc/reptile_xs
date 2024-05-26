import itertools
import requests
import json
import pandas as pd
import re
from lxml import etree, html


class TikTokProductScraper:
    def __init__(self, browserless_url, cookie_string):
        self.browserless_url = browserless_url
        self.cookies = self._parse_cookies(cookie_string)

    def _parse_cookies(self, cookie_string):
        cookies = []
        for cookie in cookie_string.split('; '):
            name, value = cookie.split('=', 1)
            cookies.append({
                "name": name,
                "value": value,
                "domain": ".dianxiaomi.com",
                "path": "/"
            })
        return cookies

    def get_html(self, product_id):
        url = f"https://www.dianxiaomi.com/tiktokProduct/edit.htm?id={product_id}"
        payload = {
            "url": url,
            "cookies": self.cookies,
            "gotoOptions": {
                "timeout": 30000,  # 超时时间设置为30秒
                "waitUntil": "networkidle0"  # 等待网络空闲状态
            }
        }
        response = requests.post(self.browserless_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page for product ID {product_id}: {response.status_code}")
            print(response.text)  # 输出错误详情
            print("网络超时，正在尝试重新请求")
            self.get_html(product_id)
            # return None

    def get_data(self, product_id):
        html_text = self.get_html(product_id)
        if not html_text:
            return None
        try:
            htmls = etree.HTML(html_text)
            data_info = self._extract_data(htmls)
            df = pd.DataFrame(data_info, index=[0])
            result = self._expand_variations(df)
            print(f"已爬取{product_id}号商品数据")
            return result
        except Exception as e:
            print(f"Error processing product ID {product_id}: {e}")
            return None

    def _extract_data(self, htmls):
        data_info = {}
        data_info['Category'] = re.sub(r'\(.*?\)', '', ''.join(
            htmls.xpath('//span[@class="category productCategory"]/span/span/text()')).replace('\xa0>\xa0', ' > ').strip())
        data_info['Brand'] = None
        data_info['Product Name'] = htmls.xpath('//*[@id="productTitle"]/@value')[0]
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
        product_images = htmls.xpath('//*[@id="myjDrop"]/li/div/div/img/@src')
        for i in range(1, 10):
            try:
                data_info[f'Product Image {i + 1}'] = product_images[i]
            except IndexError:
                data_info[f'Product Image {i + 1}'] = None
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
        data_info['Warranty Period'] = None
        data_info['UKCA/CE mark'] = None
        data_info['Product status'] = None
        return data_info

    def _expand_variations(self, df):
        result = pd.DataFrame()
        for i, row in df.iterrows():
            variations_1 = row['Variation 1'].split(',')
            variations_2 = row['Variation 2'].split(',')
            variant_images = row['Variant image'].split(',')

            max_length = max(len(variations_1), len(variant_images))
            variations_1 += [''] * (max_length - len(variations_1))
            variant_images += [''] * (max_length - len(variant_images))

            product_variations = list(itertools.product(variations_1, variations_2))
            expanded_rows = pd.DataFrame(product_variations, columns=['Variation 1', 'Variation 2'])
            expanded_rows['Variant image'] = [variant_images[i // len(variations_2)] for i in range(len(expanded_rows))]

            for col in df.columns:
                if col not in ['Variation 1', 'Variation 2', 'Variant image']:
                    expanded_rows[col] = row[col]

            result = pd.concat([result, expanded_rows], ignore_index=True)
        result = result[df.columns]
        result = result.reset_index(drop=True)
        return result


if __name__ == "__main__":
    cookie_string = "Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1716378074; _dxm_ad_client_id=A166A34BC8B6DDD9E2F8DB07B91C19FE7; dxm_i=MTYxNDQ1NSFhVDB4TmpFME5EVTEhOGZmMjc3ZmM5YWJhOGU4ZDUwZjg5ODJiNzg3NGQ5ZDQ; dxm_t=MTcxNjQzMzIxMiFkRDB4TnpFMk5ETXpNakV5ITRiZTg2Njk3OGM5YzdjNTc5YTRhOTQ4MGNjMTM1OWRj; dxm_c=YzZVWXJMd1QhWXoxak5sVlpja3gzVkEhOTk5Y2NjOTAxOGZkYzJhYzMyNWRlYTI3ZWM4Zjc3MjU; dxm_w=ZDEwYTcwMTA5Yzg2YTM2ZTgwMzJmZWRkYWFiOWFmYjchZHoxa01UQmhOekF4TURsak9EWmhNelpsT0RBek1tWmxaR1JoWVdJNVlXWmlOdyE3N2M1OWYzYTk5YWFkMmVjMzg3YjhmOTdhOWFkYTQxNg; dxm_s=rav-G5sVoKDLJtw3LWk6GgWHV_Qrlb0ch38bNzGvEk8; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1716449026; JSESSIONID=AC81388D44A14E4F5EC5074EBEBDB321"
    scraper = TikTokProductScraper("http://110.40.40.22:3000/content", cookie_string)
    product_ids = input("TikTok ID: ").split(",")
    print("开始爬取数据")
    df_list = []
    for product_id in product_ids:
        data = scraper.get_data(product_id)
        if data is not None:
            df_list.append(data)
    if df_list:
        df = pd.concat(df_list, ignore_index=True)
        df.to_excel("tiktok_products.xlsx", index=False)
        print("数据已保存至 tiktok_products.xlsx")
    else:
        print("没有获取到任何数据")

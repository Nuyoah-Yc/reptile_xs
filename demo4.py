from lxml import etree

html_1 = '''
<div class="con-options attrOptionsBox">
    <div class="change-box-out changeBoxOut">
        <label>
            <input type="checkbox" value="320035006F007A002F003700350030006D006C00" data-type="&amp;{themeType}" checked="" data-valid="25oz/750ml">
            <span class="changeIcon" style="border: 1px solid rgb(238, 238, 238); display: inline-block; position: relative; top: 2px; width: 14px; height: 14px; margin-right: 5px; background-image: url(&quot;/static/img/productSize/custom_variantImage.png&quot;); background-size: cover;"></span>
            <span class="name changeName">25oz/750ml</span>
        </label>
        <div class="change-box changeBox">
            <span class="attach-icons md-18 btnEdit" title="编辑">edit</span>
        </div>
    </div>
    <div class="change-box-out changeBoxOut">
        <label>
            <input type="checkbox" value="330032006F007A002F0031003000300030006D006C00" data-type="&amp;{themeType}" checked="" data-valid="32oz/1000ml">
            <span class="changeIcon" style="border: 1px solid rgb(238, 238, 238); display: inline-block; position: relative; top: 2px; width: 14px; height: 14px; margin-right: 5px; background-image: url(&quot;/static/img/productSize/custom_variantImage.png&quot;); background-size: cover;"></span>
            <span class="name changeName">32oz/1000ml</span>
        </label>
        <div class="change-box changeBox">
            <span class="attach-icons md-18 btnEdit" title="编辑">edit</span>
        </div>
    </div>
    <div class="change-box-out changeBoxOut">
        <label>
            <input type="checkbox" value="310037006F007A002F003500300030006D006C00" data-type="&amp;{themeType}" checked="" data-valid="17oz/500ml">
            <span class="changeIcon" style="border: 1px solid rgb(238, 238, 238); display: inline-block; position: relative; top: 2px; width: 14px; height: 14px; margin-right: 5px; background-image: url(&quot;/static/img/productSize/custom_variantImage.png&quot;); background-size: cover;"></span>
            <span class="name changeName">17oz/500ml</span>
        </label>
        <div class="change-box changeBox">
            <span class="attach-icons md-18 btnEdit" title="编辑">edit</span>
        </div>
    </div>
</div>
'''

html_2 = '''
<div class="con-options attrOptionsBox">
    <label class="size-item items"><input type="checkbox" value="5300" data-valid="">S</label>
    <label class="size-item items"><input type="checkbox" value="58004C00" data-valid="">XL</label>
    <label class="size-item items"><input type="checkbox" value="4C00" data-valid="">L</label>
    <label class="size-item items"><input type="checkbox" value="4D00" data-valid="">M</label>
    <label class="size-item items"><input type="checkbox" value="580058005300">XXS</label>
    <label class="size-item items"><input type="checkbox" value="58005300">XS</label>
    <label class="size-item items"><input type="checkbox" value="580058004C00">XXL</label>
    <label class="size-item items"><input type="checkbox" value="5800580058004C00">XXXL</label>
    <label class="size-item items"><input type="checkbox" value="58005800580058004C00">XXXXL</label>
    <label class="size-item items"><input type="checkbox" value="580058005800580058004C00">XXXXXL</label>
</div>
'''


def get_checked_options(html, label_xpath=None):
    tree = etree.HTML(html)
    checked_options = []

    # 寻找所有被选中的复选框
    for checkbox in tree.xpath('//input[@type="checkbox" and @checked]'):
        value = checkbox.get('value')

        # 尝试获取复选框对应的标签文本
        if label_xpath:
            label = checkbox.xpath(label_xpath)
        else:
            label = checkbox.xpath('following-sibling::text()')

        if label:
            label = label[0].strip()
        else:
            label = '未知'

        checked_options.append((value, label))

    return checked_options


# 对于甲页面，指定正确的 XPath 表达式以获取标签文本
checked_options_1 = get_checked_options(html_1, 'following-sibling::span[@class="name"]/text()')
# 对于乙页面，修复代码以考虑所有的复选框是否被勾选
checked_options_2 = get_checked_options(html_2, '../../text()')

print("甲页面已勾选项：", checked_options_1)
print("乙页面已勾选项：", checked_options_2)

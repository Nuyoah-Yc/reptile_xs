import pandas as pd
import itertools

# 读取CSV文件
df = pd.read_csv('data.csv')

# 将需要拆分的列按逗号拆分
df['Variation 1'] = df['Variation 1'].str.split(',')
df['Variation 2'] = df['Variation 2'].str.split(',')
df['Variant image'] = df['Variant image'].str.split(',')

# 初始化一个空的DataFrame来存储结果
result = pd.DataFrame()

# 对每一行进行处理
for i, row in df.iterrows():
    variations_1 = row['Variation 1']
    variations_2 = row['Variation 2']
    variant_images = row['Variant image']

    # 确保Variation 1和Variant image数量一致，不足则填充为空
    max_length = max(len(variations_1), len(variant_images))
    variations_1 += [''] * (max_length - len(variations_1))
    variant_images += [''] * (max_length - len(variant_images))

    # 生成Variation 1和Variation 2的笛卡尔积
    product_list = list(itertools.product(variations_1, variations_2))

    # 生成包含Variation 1, Variation 2和Variant image的DataFrame
    expanded_rows = pd.DataFrame(product_list, columns=['Variation 1', 'Variation 2'])
    expanded_rows['Variant image'] = [variant_images[i % len(variant_images)] for i in range(len(expanded_rows))]

    # 将其他列的值重复添加到笛卡尔积中
    for col in df.columns:
        if col not in ['Variation 1', 'Variation 2', 'Variant image']:
            expanded_rows[col] = row[col]

    # 将处理后的行添加到结果中
    result = pd.concat([result, expanded_rows], ignore_index=True)

# 确保列名顺序正确
result = result[df.columns]

# 重置索引以保持数据整洁
result = result.reset_index(drop=True)

# 将处理后的数据保存到新文件
result.to_csv('data_exploded.csv', index=False)

# 打印处理后的数据
print(result)

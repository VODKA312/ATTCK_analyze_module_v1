import pandas as pd

# 读取数据文件
data = pd.read_excel("./DataSource/test.xlsx")  # 替换为你的数据文件路径
# 总的技术种类列
total_techniques = data.columns[3:]  # 假设总的技术种类列从第4列开始

print(total_techniques)
# 遍历每一行数据
for index, row in data.iterrows():
    # 获取当前行的target id，是单个变量
    target_id = row["target ID"]
    # 设置索引
    index_column = 0
    # 遍历总的技术种类列
    for column in total_techniques:
        # 判断target id下的技术种类是否存在于总的技术种类列中
        if target_id in column:
            # 在存在的技术种类列中填充1
            # print(data.iloc[index, index_column+3])
            data.iloc[index, index_column+3] = 1
        else:
            # 在不存在的技术种类列中填充0
            # print(data.iloc[index, index_column+3])
            data.iloc[index, index_column+3] = 0
        index_column = index_column + 1

# 保存修改后的数据
data.to_excel("./DataSource/test_3.xlsx", index=False)  # 替换为你想保存的文件路径，index=False表示不保存索引
import pandas as pd
# 读取整个 Excel 文件
xls = pd.ExcelFile("./DataSource/new_attck_relationship.xlsx")
# 获取所有子表的名称
sheet_names = xls.sheet_names
#先获取technique子表中所有的technique信息
selected_sheet = sheet_names[1]  # 假设选择第一个子表

# 读取选择的子表数据
df_technique = pd.read_excel(xls, selected_sheet)
# 获取 ID 列的所有数据并放入列表
id_list = df_technique['ID'].tolist()
# 选择要读取的特定子表——group_use_technique
selected_sheet = sheet_names[0]  # 假设选择第一个子表
# 读取选择的子表数据
df_group_technique = pd.read_excel(xls, selected_sheet)
# 创建一个空字典用于构建JSON数据
json_data = {}

# 遍历每个group
for group in df_group_technique['source ID'].unique():
    # 获取当前group的数据
    group_data = df_group_technique[data['source ID'] == group]

    # 构建group的技术列表
    techniques = group_data['target ID'].tolist()

    # 将group和对应的技术列表添加到JSON字典中
    json_data[group] = techniques

# 将JSON字典转换为JSON字符串
json_str = pd.io.json.dumps(json_data, indent=4)

# 打印JSON字符串
print(json_str)

# 创建一个空的DataFrame作为新的Excel表格
df = pd.DataFrame(columns=['source ID'] + id_list)

# 创建空行，所有technique_id种类的列都填充为0
empty_row = {column: 0 for column in id_list}

# 遍历JSON数据中的每个group和对应的technique_id列表
for group, techniques in json_data.items():
    # 复制空行，用作当前group的一行数据
    row = empty_row.copy()
    row['source ID'] = group

    # 在每个technique_id种类列中填充1
    for technique in techniques:
        if technique in id_list:
            row[technique] = 1

    # 将当前行添加到结果DataFrame中
    df = df.append(row, ignore_index=True)
# 将结果保存到Excel表格
df.to_excel('./DataSource/result.xlsx', index=False)

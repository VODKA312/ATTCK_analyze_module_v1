import json
import pandas as pd

# 读取JSON文件
with open('../clustering/frequency_id.json', 'r') as json_file:
    data = json.load(json_file)
    
def generate_technique_relations(data, min_usage_count):
    # 过滤出usage_count大于25的数据
    filtered_data = [entry for entry in data if entry['usage_count'] > min_usage_count]

    # 提取technique_id
    technique_ids = [entry['technique_id'] for entry in filtered_data]

    # 生成两两组合
    combinations = []
    # 遍历给定的列表并将元素两两关联
    for i in range(len(technique_ids)):
        for j in range(i + 1, len(technique_ids)):
            for item1 in technique_ids[i]:
                for item2 in range(i + 1, len(technique_ids[i])):
                    combinations.append((item1, technique_ids[i][item2]))
                for item3 in technique_ids[j]:
                    combinations.append((item1, item3))

    # 创建数据框
    df = pd.DataFrame(combinations, columns=['technique_id_1', 'technique_id_2'])

    return df

# 调用函数并生成excel文件
result_df = generate_technique_relations(data, 25)
result_df = result_df.drop_duplicates()
result_df.to_excel('../DataSource/high_frequency_technique.xlsx', sheet_name='frequency_25', index=False, engine='openpyxl')
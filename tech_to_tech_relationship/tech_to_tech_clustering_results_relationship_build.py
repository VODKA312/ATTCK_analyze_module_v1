import json
import pandas as pd

# 读取JSON文件
with open('../clustering/frequency_id.json', 'r') as json_file:
    data = json.load(json_file)

# 过滤出usage_count大于25的数据
filtered_data = [entry for entry in data if entry['usage_count'] > 25]

# 提取technique_id
technique_ids = [entry['technique_id'] for entry in filtered_data]

high_frequency_id = []
for i in technique_ids:
    for j in i:
        high_frequency_id.append(j)

# 读取JSON文件
with open('../clustering/cluster_data_pre0_cutoff4.json', 'r') as json_file:
    data_clustering = json.load(json_file)
# 创建一个空的DataFrame来存储technique_id_1和technique_id_2
columns = ['technique_id_1', 'technique_id_2']
result_df = pd.DataFrame(columns=columns)

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

result_df = generate_technique_relations(data, 25)
result_df = result_df.drop_duplicates()

# 统计高频节点不存在的次数
high_frequency_not_exist = 0

# 遍历聚类数据
for cluster_id, techniques in data_clustering.items():
    high_frequency_present = False  # 标志是否有Technique在high_frequency_id列表中
    
    # 检查聚类中的每个Technique是否至少有一个在high_frequency_id列表中
    for technique in techniques:
        if technique in high_frequency_id:
            high_frequency_present = True
            break
    
    # 如果至少有一个Technique在high_frequency_id列表中，构建关系
    if high_frequency_present:
        for i in range(len(techniques)):
            print(techniques[i])
            for j in range(i + 1, len(techniques)):
                result_df = result_df.append({'technique_id_1': techniques[i], 'technique_id_2': techniques[j]}, ignore_index=True)
    else:
        # 如果聚类中没有Technique在high_frequency_id列表中，增加计数
        high_frequency_not_exist += 1 

print(high_frequency_not_exist)
print(result_df)

result_df = result_df.drop_duplicates()
result_df.to_excel('../DataSource/technique_relations_cluster_data_pre0_cutoff4.xlsx', sheet_name='inner_relationship', index=False, engine='openpyxl')


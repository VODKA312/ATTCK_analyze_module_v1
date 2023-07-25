import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from phik import phik_matrix
from scipy.spatial.distance import squareform
#读取源数据
data = pd.read_excel("../DataSource/result.xlsx")
# 去除 'source ID' 列
data = data.drop('source ID', axis=1)
data_array = data.values
# 计算样本之间的Phi系数距离矩阵
def phi_coefficient_distance(X):
    # 将NumPy数组转换为Pandas DataFrame对象
    X_df = pd.DataFrame(X, columns=data.columns)
    phi_matrix = phik_matrix(X_df.select_dtypes(include=['int64', 'bool']))  # 选择合适的数据类型进行计算
    return phi_matrix
# 初始化一个空的距离矩阵
distance_matrix = np.zeros((data_array.shape[0], data_array.shape[0]))

# 分批计算样本之间的Phi系数距离矩阵
batch_size = 75
for i in range(0, data_array.shape[0], batch_size):
    start_idx = i
    end_idx = min(i + batch_size, data_array.shape[0])

    # 计算当前批次内样本之间的Phi系数距离
    batch_distance = phi_coefficient_distance(data_array[start_idx:end_idx])

    # 将批次内的距离矩阵转换成一维形式，再填充到整体距离矩阵中
    distance_matrix.reshape[-1,1] = squareform(batch_distance)

# 使用Ward链接法进行聚类
n_clusters = 16
cluster = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='ward')
cluster_labels = cluster.fit_predict(distance_matrix)

print(cluster_labels)
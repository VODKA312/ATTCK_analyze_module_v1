from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

def hopkins(X):
    n = X.shape[0]  # 数据集中样本点的数量
    d = X.shape[1]  # 数据集中每个样本点的维度

    # 计算样本点之间的距离矩阵
    nbrs = NearestNeighbors(n_neighbors=1).fit(X)
    distances, _ = nbrs.kneighbors(X)
    rand_X = np.random.uniform(low=X.min(axis=0), high=X.max(axis=0), size=(n, d))

    # 计算样本点与随机点之间的距离矩阵
    nbrs_rand = NearestNeighbors(n_neighbors=1).fit(rand_X)
    rand_distances, _ = nbrs_rand.kneighbors(rand_X)

    # 计算Hopkins统计量
    u = distances.sum()
    w = rand_distances.sum()
    hopkins_statistic = u / (u + w)

    return hopkins_statistic

# 数据标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 计算霍普金斯统计量
hopkins_statistic = hopkins(X)
print("Hopkins Statistic:", hopkins_statistic)
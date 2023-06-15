import jieba
import numpy as np
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# 读取文本数据
with open(r'C:\Users\YZYhhh\Desktop\TM\database\wordbase\【原神】游戏词库.txt', 'r', encoding='utf-8') as f:
    texts = f.readlines()

# 构建相似矩阵
# 加载SentenceTransformer模型
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# 对文本进行汇集编码,生成向量表示
embeddings = model.encode(texts, show_progress_bar=True)

# 根据向量构建cosine相似矩阵
similarity_matrix = cosine_similarity(embeddings)

# 随机游走
frequencies = np.zeros(len(texts))
walked = [0]
while len(walked) < len(texts):
    idx = walked[-1]
    scores = similarity_matrix[idx]
    most_similar = np.argmax(scores)
    walked.append(most_similar)
    # ... 根据相似矩阵进行随机游走,记录

# 聚类
clusters = KMeans(n_clusters=6).fit_predict(scores.reshape(-1,1))

# 分组结果
for i in range(6):
    group = [texts[j] for j in np.where(clusters==i)[0]]
    print('cluster {}:'.format(i))
    print(group)
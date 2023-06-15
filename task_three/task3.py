import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder

# 1.读取数据
data = pd.read_csv(r'C:\Users\YZYhhh\Desktop\TM\database\data.csv', dtype={'text':object})

# 2.TF-IDF降维
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(data['text'])

# 3.划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, data['label'], test_size=0.2)

# 4.建模与预测
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# 5.PCA降维SS
# pca = PCA(n_components=2)
# X_reduced = pca.fit_transform(X)

svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X)

# 6.可视化
label_map = {'positive':0, 'negative':1}
data['label'] = data['label'].map(label_map)
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])
plt.scatter(X_reduced[:,0], X_reduced[:,1], c= data['label'])
plt.show()
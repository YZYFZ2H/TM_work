import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 下载语料库
# nltk.download('gutenberg')

# 加载文本数据
text = nltk.corpus.gutenberg.raw('shakespeare-macbeth.txt')

# 分词和词汇过滤
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
tokens = [t for t in tokens if t.isalpha() and t not in stop_words]

# 抽取词汇
finder = BigramCollocationFinder.from_words(tokens)
bigram_measures = BigramAssocMeasures()
scored = finder.score_ngrams(bigram_measures.raw_freq)
n = 100
top_n_bigrams = [bigram for bigram, score in scored][:n]
print(top_n_bigrams)

# 特征提取和模型训练
count_vect = CountVectorizer(vocabulary=top_n_bigrams)
X_train_counts = count_vect.fit_transform([text])
clf = MultinomialNB().fit(X_train_counts, [0])

# 验证新词汇
new_text = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
X_new_counts = count_vect.transform([new_text])
predicted = clf.predict(X_new_counts)
print(predicted)

# 更新词典
if predicted[0] == 1:
    print("该文本属于高频二元组")
    with open(r"C:\Users\YZYhhh\Desktop\TM\task_two\my_dict.txt", "a") as f:
        f.write(new_text + "\n")
else:
    print("该文本不属于高频二元组")
from sklearn.decomposition import TruncatedSVD
from gensim import corpora, models




# LSI模型 
model = TruncatedSVD(n_components=10)
user_vec = model.fit_transform(user_data)

# # LDA模型
# dictionary = corpora.Dictionary(user_data)
# corpus = [dictionary.doc2bow(text) for text in user_data]
# ldamodel = models.ldamodel.LdaModel(corpus, num_topics)
# user_vec = ldamodel[corpus]



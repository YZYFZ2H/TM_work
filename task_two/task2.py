import jieba.posseg
import os.path
from collections import defaultdict

dic_root_path = os.getcwd() + '/res/dic/'         #情感词典的根目录

neg_corpus_root_path = os.getcwd() + '/Emotion_Manager/Modules/res/corpus/hotel/neg/'  #酒店评价负面情绪语料库目录
pos_corpus_root_path = os.getcwd() + '/Emotion_Manager/Modules/res/corpus/hotel/pos/' #酒店评价正面情绪语料库目录
sense_word_kind_set = {}                #具有情感的词性集合

with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\dic\zhiwang\pos_comment.txt', 'r', encoding="utf-8") as f:
    content_pos = f.read()
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\comment.txt', 'a', encoding="utf-8") as f:
    f.write(content_pos)
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\dic\zhiwang\neg_comment.txt', 'r', encoding="utf-8") as f:
    content_neg = f.read()
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\comment.txt', 'a', encoding="utf-8") as f:
    f.write(content_neg)
    #  至此，comment.txt包含了所有的正向负向情绪词语

with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\comment.txt', 'r', encoding="utf-8") as f:
    com_emo_dict = set([line.strip() for line in f])
    print("现在字典长度：" + str(len(com_emo_dict)))

#  测试
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\corpus\neg_all.txt', 'r', encoding="utf-8") as f:
    corpus = f.read()

with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\corpus\pos_all.txt', 'r', encoding="utf-8") as f:
    haha = f.read()
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\record.txt', 'a', encoding="utf-8") as f:
    f.write(corpus)
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\record.txt', 'a', encoding="utf-8") as f:
    f.write(haha)

with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\record.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
non_empty_lines = [line for line in lines if line.strip() != ""]
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\record.txt', 'w', encoding="utf-8") as f:
    f.writelines(non_empty_lines)
with open(r'C:\Users\YZYhhh\Desktop\TM\task_two\res\record.txt', 'r', encoding="utf-8") as f:
    record = f.read()
    #  至此，record包含了所有的正向负向评论

# corpus ='''服务态度极其差，前台接待好象没有受过培训，连基本的礼貌都不懂，竟然同时接待几个客人；
# 大堂副理更差，跟客人辩解个没完，要总经理的电话投诉竟然都不敢给。要是没有作什么亏心事情，跟本不用这么怕。'''
for i in range(3): #循环次数自定义
    dict_num = com_emo_dict
    # 分词并过滤出情感词汇
    tokens = jieba.lcut(record) #或corpus
    com_emo_tokens = set(tokens) & com_emo_dict

    # 统计词汇的词频
    freq_dict = {}
    for token in com_emo_tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1

    # 输出前5个高频词汇
    sorted_freq = sorted(freq_dict.items(), key=lambda x: -x[1])
    print("前5高频词如下：")
    for token, freq in sorted_freq[:5]:
        print(token, freq)

    # 统计所有词汇的出现次数
    all_tokens = jieba.lcut(corpus)
    all_freq_dict = defaultdict(int)
    for token in all_tokens:
        all_freq_dict[token] += 1

    # 对词典中的所有词，找到其空间索引中的K近邻，得到新词集合
    new_tokens = set()
    for token in com_emo_dict:
        if token in all_freq_dict:
            # 计算相似度
            sim_dict = {t: count for t, count in all_freq_dict.items() if t != token}
            sim_dict = {t: count / (all_freq_dict[t] + all_freq_dict[token] - count) for t, count in sim_dict.items()}
            # 按相似度从高到低排序
            sorted_sim = sorted(sim_dict.items(), key=lambda x: -x[1])
            # 取前100个相似度最高的词
            new_tokens |= {t for t, sim in sorted_sim[:100] if sim > 0.5 and all_freq_dict[t] > 10}

    #  对新词集合中的词，检查其TF，以及DF，对于满足条件的新词，加入到词典中
    new_com_emo_tokens = set()
    docs = corpus

    for token in new_tokens:
        if all_freq_dict[token] >= 5 and all_freq_dict[token] <= 10000:
            # 计算DF
            df = sum(1 for doc in docs if token in doc)
            if df >= 3:
                new_com_emo_tokens.add(token)

    # 将新词加入到词典中
    com_emo_dict |= new_com_emo_tokens
    print("第%s轮更新完成" % str(i+1))
    print("更新后字典长度：" +str(len( com_emo_dict)))

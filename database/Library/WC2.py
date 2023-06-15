from wordcloud import WordCloud
import matplotlib.pyplot as plt
# from scipy.misc import imread # scipy中已经找不到该函数了，因为scipy版本>=1.3.0已经移除了

# import imageio # 使用该代码可能会出现一个小的warning，改成下面的格式就行
import imageio.v2 as imageio
img = imageio.imread(r'C:\Users\YZYhhh\Desktop\TM\Photo\shuangzi.jpg')

file_path = 'my_file.txt'

# 打开文件并读取内容
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

wc = WordCloud(background_color='white',
                      width=800,
                      height=600,
                      max_words=200,
                      max_font_size=80,
                      mask=img)
wc.generate(text)

wc.to_file('output.png')

plt.show()
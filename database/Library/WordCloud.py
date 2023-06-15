from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
# 指定文件路径
file_path = 'my_file.txt'
# 打开文件并读取内容
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
mask = np.array(Image.open(r"C:\Users\YZYhhh\Desktop\TM\Photo\zhong_ren.jpg"))
# 创建 WordCloud 对象
wordcloud = WordCloud(background_color="white", mask=mask, contour_width=3, contour_color="steelblue")
# 生成词云图
wordcloud.generate(text)
# 从图像颜色中提取颜色
image_colors = ImageColorGenerator(mask)
# 绘制词云图
plt.figure(figsize=[10,10])
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
# 展示图像
plt.show()


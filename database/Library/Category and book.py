import requests
import os
import sys
import numpy as np
from bs4 import BeautifulSoup
category = 'http://books.toscrape.com/catalogue/category'  # 定义目录地址
UNIT_PATH = r'C:\Users\YZYhhh\Desktop\TM\database\Library\UNIT' #定义数目类别文件夹路径
Library_Path = r'C:\Users\YZYhhh\Desktop\TM\database\Library'

#  基本操作复习
res = requests.get('http://books.toscrape.com/catalogue/category/books_1/index.html') # 输入首页网址
html = res.text #文本化
soup = BeautifulSoup(html, 'html.parser') #解析
items = soup.find_all('article',class_='product_pod') #这是针对找到对应类别网页之后提取网页文章信息的前提

# 获取各类读物网址
books = soup.find('ul', class_='nav').find('ul').find_all('a') # 这是准备提取目录各个书目网址的前提
h_sum = []
TT_SUM = []
bp = []
for book in books:  # 获取目录书类别网址操作
    #print(book.text.strip()) #  先输出目录书目类别名称
    bp.append(book.text.strip())
    b_h = book['href']
    #  print(b_h)
    b_h_real = b_h[2:] #　取出的网址有＂．．＂需要删除＂．．＂以免影响后面网址拼接
    h_h = [category + str(b_h_real)] #  网址拼接，h_h储存了对应目录类别的网址
    #print(h_h) #  输出网址看看，发现确实是可以到达的网址
    for element in h_h:
        h_sum.append(element)
        #print(h_sum)
        cwd = r'C:\Users\YZYhhh\Desktop\TM\database\Library\Category'
        file_name = book.text.strip()
        file_path = os.path.join(cwd, file_name)
        with open(file_path, "w", encoding='utf-8') as f:
            f.write("%s\n" % element)

        # 指定路径和文件夹名称
        path = r'C:\Users\YZYhhh\Desktop\TM\database\Library\UNIT'
        folder_name = book.text.strip()
        # 使用os.mkdir()函数创建文件夹
        #new_folder_path = os.path.join(path, folder_name)
        #os.mkdir(new_folder_path)

# 获取具体某类读物网址下读物信息
for hhh in h_sum:
    HRE = requests.get(hhh)
    HTML = HRE.text
    SOUP = BeautifulSoup(HTML, 'html.parser')
    Items = SOUP.find_all('article', class_='product_pod') #这是针对找到对应类别网页之后提取网页文章信息的前提
    print('add: ' + hhh) #检查是否添加成功-->确实成功

    for Item in Items: # 每个类别的书目/书名识别
        name = Item.find('h3').find('a')
        TITLE = name['title']  # 输出书名--一串
        TT_SUM.append(TITLE) # 保存所有读到的书名

print(TT_SUM)

# with open('my_file.txt', 'w', encoding='utf-8') as f:
#     for item in TT_SUM:
#         f.write(f'{item.strip()}\n')
# 至此保存了将近500本图书资源

# for i in range(len(bp)):
    #     unit_path = os.path.join(UNIT_PATH, bp[i])
    #     with open(unit_path, "w", encoding='utf-8') as f:
    #         for tit in TITLE:
    #             f.write("%s\n" % tit)


            #print(TT_SUM)

    # cwd = r'C:\Users\YZYhhh\Desktop\TM\database\Library'
    # file_name = TITLE + 'txt'
    # file_path = os.path.join(cwd, file_name)
#
#     with open(file_path, "w", encoding = 'utf-8') as f:
#         list_star = Item.find('p', class_="star-rating")
#         RATE = 'star-rating is: ' + list_star['class'][1]#  输出星级
#         print(RATE)
#
#         PRICE = Item.find('p', class_="price_color")#  输出价格
#         P_T = PRICE.text
#         print(P_T)
#
#         f.write("%s\n%s" % (RATE, P_T))


# for item in items:
#     name=item.find('h3').find('a')
#     list_star=item.find('p',class_="star-rating")
#     price=item.find('p',class_="price_color")
#
#     print(name['title']) #输出书名
#     print('star-rating is :',list_star['class'][1]) #输出星级
#     print(price.text)  #输出价格
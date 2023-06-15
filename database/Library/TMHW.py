import requests
from bs4 import BeautifulSoup
res = requests.get('https://zhuanlan.zhihu.com/p/327925267')
bs_books = BeautifulSoup(res.text, 'html.parser')
list_books = bs_books.find_all('img')
print(list_books,end='\n')

#,  class_='position-list__item home-channel__red--point position-list__item--first'
for tag_books in list_books:
    #tag_name = tag_books.find('src')
    #list_star = tag_books.find('h2', class_="entry-title")
#    tag_a = tag_books.find('a')
    print(tag_books['src']) # 这里用到了tag['属性名']提取属性值
    #print(list_star.text)
#    print(tag_a['title'], end='\n'+'------'+'\n')
    #class ="position-list__item home-channel__red--point position-list__item--first"
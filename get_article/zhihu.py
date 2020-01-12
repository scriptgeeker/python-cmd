# pip install requests
# pip install bs4
# pip install lxml

import requests
from bs4 import BeautifulSoup
import lxml

url = input('URL:')

dir = r'C:\Users\BenQ\Downloads'

# 访问伪装
user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/76.0.3809.132 Safari/537.36')

headers = {'User-Agent':user_agent}

# 发送请求
response = requests.get(url,headers=headers)
assert response.status_code == 200

title,author,content = '','',''
soup = BeautifulSoup(response.text, 'lxml')

# 获取内容
title = soup.select('h1.QuestionHeader-title')[0].get_text()
author = soup.select('div.AuthorInfo-head div.Popover a')[0].get_text()
for ele in soup.select('div.RichContent-inner .RichText')[0].children:
    content = content + ele.get_text() + '\n'

# 处理文本
import re
content = re.sub(r'\s{2,}', '\n', content)

# 创建目录
import os
if not os.path.exists(dir):
    os.makedirs(path)

file = '{a}-{b}的回答.txt'.format(a=title,b=author)
path = os.path.join(dir,file)

# 写入文件
fw = open(path, 'w', encoding='utf8')
fw.write(content)
fw.close()

print(os.path.abspath(path))
# pip install requests
# pip install bs4
# pip install lxml

import requests
from bs4 import BeautifulSoup
import lxml

url = input('URL:')

path = r'C:\Users\BenQ\Downloads'

# 访问伪装
user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
              'AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/76.0.3809.132 Safari/537.36')

headers = {'User-Agent': user_agent}

# 发送请求
response = requests.get(url, headers=headers)
assert response.status_code == 200

title, label, content = '', '', ''
soup = BeautifulSoup(response.text, 'lxml')

# 获取内容
title = soup.select('h2#activity-name')[0].get_text()
label = soup.select('a#js_name')[0].get_text()

for ele in soup.select('div#js_content')[0].children:
    try:
        content = content + ele.get_text() + '\n'
    except Exception as e:
        continue

# 处理文本
import re

title = re.sub(r'\s', '', title)
label = re.sub(r'\s', '', label)
content = re.sub(r'\s{2,}', '\n', content)

# 创建目录
import os

if not os.path.exists(path):
    os.makedirs(path)

file = path + '/' + '【{a}】{b}.txt'.format(a=label, b=title)

# 写入文件
fw = open(file, 'w', encoding='utf8')
fw.write(content)
fw.close()

print(os.path.abspath(file))

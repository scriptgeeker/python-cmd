import requests
from bs4 import BeautifulSoup
import lxml

url = input('URL:')

path = r'C:\Users\BenQ\Downloads'

# 访问伪装
user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/76.0.3809.132 Safari/537.36')

# 设置代理
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

headers = {'User-Agent':user_agent}

# 发送请求
response = requests.get(url,headers=headers,proxies=proxies)
assert response.status_code == 200

title,content = '',''
soup = BeautifulSoup(response.text, 'lxml')

# 获取内容
title = soup.select('div.post h1.post-title')[0].get_text()
content = soup.select('div.post div.post-body')[0].get_text()


# 处理文本
import re
title = re.sub(r'\s','',title)
content = re.sub(r'\s{2,}', '\n', content)

# 创建目录
import os
if not os.path.exists(path):
    os.makedirs(path)

file = path + '/' + title + '.txt'

# 写入文件
fw = open(file, 'w', encoding='utf8')
fw.write(content)
fw.close()

print(os.path.abspath(file))
import requests
from bs4 import BeautifulSoup

# 1. 发送请求获取网页内容
url = "https://www.baidu.com"
response = requests.get(url)

# 2. 检查是否请求成功
if response.status_code == 200:
    # 3. 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 4. 提取网页标题（<title> 标签里的内容）
    title = soup.find('title').get_text()

    # 5. 打印标题
    print("网页标题是：", title)
else:
    print("请求失败，状态码：", response.status_code)
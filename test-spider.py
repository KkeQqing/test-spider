from bs4 import BeautifulSoup
from safe_requests import safe_get

# 使用 safe_get 获取百度首页
result = safe_get("https://www.baidu.com")

if result['success']:
    soup = BeautifulSoup(result['data'], 'html.parser')
    title = soup.find('title')
    print("标题：", title.get_text() if title else "无标题")
else:
    print("❌ 获取失败：", result['error'])

# 获取今日诗词
result = safe_get("https://v1.jinrishici.com/all.json", return_json=True)

if result['success']:
    data = result['data']

    # ✅ 正确判断：看是否包含诗词内容
    if isinstance(data, dict) and data.get('content'):
        print("📜 今日诗词：")
        origin = data.get('origin', '无题')
        author = data.get('author', '佚名')
        dynasty = data.get('dynasty', '')  # 注意：该 API 实际不返回 dynasty！
        content = data['content']

        print(f"《{origin}》")
        if dynasty:
            print(f"—— {author}〔{dynasty}〕")
        else:
            print(f"—— {author}")
        print(content)
    else:
        print("❌ API 返回数据异常，未找到诗词内容")
        print("原始返回：", data)
else:
    print("❌ 网络请求失败：", result['error'])

# 使用自定义请求头
custom_headers = {
    'Referer': 'https://www.google.com',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

result = safe_get("https://example.com", headers=custom_headers)
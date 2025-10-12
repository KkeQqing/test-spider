# 安全网络请求工具包

本项目提供一个健壮、可复用的 HTTP 请求封装函数 `safe_get`，适用于网络爬虫、API 调用等场景，具备异常处理、自动重试和浏览器伪装能力。

---

## 📦 环境依赖

| 包名             | 版本   |
| ---------------- | ------ |
| `python`         | 3.13.7 |
| `requests`       | 2.32.5 |
| `beautifulsoup4` | 4.13.5 |

### 创建 Conda 环境

1. 将 `environment.yml` 文件置于项目根目录。  
2. 在 **Anaconda Prompt** 中运行：

```bash
conda env create -f environment.yml
```

Conda 将自动：
- 读取文件中的 `name` 作为环境名。
- 安装指定的 Python 版本。
- 安装所有列出的依赖包。

> 💡 **PyCharm 用户**：将 `environment.yml` 放在项目根目录后，直接在 PyCharm 中打开项目，IDE 会自动提示创建并安装所需环境。

---

## 📁 核心文件说明

### `safe_requests.py`

封装了一个可复用、带重试机制的通用“安全请求函数”。

#### 主要功能

- ✅ 自动添加 `User-Agent`（支持自定义）
- ✅ 支持超时控制（默认 10 秒）
- ✅ 捕获所有常见网络异常（如超时、连接错误、DNS 失败等）
- ✅ 可选自动重试机制（默认失败后重试 2 次，支持指数退避）
- ✅ 返回结构化结果（包含 `success`、`data`、`error` 等字段）
- ✅ 兼容 `requests.Response` 对象，便于后续解析（如配合 BeautifulSoup）

---

## 🌐 常量：`BROWSER_HEADERS`

定义了一组标准浏览器请求头，用于模拟真实用户访问，有效绕过基础反爬策略。

```python
BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
```

### 各字段详解

#### 1. `User-Agent`
- **作用**：标识客户端身份。
- **为什么重要？**  
  多数网站会拒绝 `python-requests` 默认的 User-Agent（如 `python-requests/2.32.5`），认为是爬虫。

#### 2. `Accept`
- **作用**：声明客户端可接受的内容类型及优先级。
- **典型值**：优先 HTML，支持 WebP 图片，兜底接受任意类型。

#### 3. `Accept-Language`
- **作用**：指定语言偏好。
- **效果**：支持多语言的网站（如百度、知乎）将优先返回中文内容。

#### 4. `Accept-Encoding`
- **作用**：声明支持的压缩算法（`gzip`, `deflate`, `br`）。
- **注意**：`requests` 会自动解压响应，你获取的 `response.text` 始终是明文。

#### 5. `Connection: keep-alive`
- **作用**：复用 TCP 连接，提升性能。
- **意义**：模拟真实浏览器行为，降低被识别为爬虫的风险。

#### 6. `Upgrade-Insecure-Requests: 1`
- **作用**：请求将 HTTP 资源自动升级为 HTTPS。
- **适用场景**：现代 HTTPS 网站常检查此头，缺失可能被视为旧客户端。

---

## ✅ 使用建议

- 在所有对外 HTTP 请求中使用 `safe_get`，避免程序因网络异常崩溃。
- 对普通网页抓取，直接使用 `BROWSER_HEADERS` 即可有效伪装。
- 对 JSON API，可根据需要简化 headers（通常保留 `User-Agent` 即可）。
- 始终设置合理的超时时间，防止请求长时间阻塞。

---

> 📌 **提示**：本工具适用于基础反爬场景。如遇动态渲染、登录验证、验证码等高级防护，建议结合 Selenium、Playwright 或代理池方案。
```
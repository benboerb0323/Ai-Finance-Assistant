# AI金融助手

这是一个基于 Flask + SQLite + DeepSeek API 开发的 AI 金融问答 Web 应用。项目以“银行 AI 助手”为场景，用户可以在网页中输入理财、基金、债券、工资规划等问题，系统会调用 AI 模型生成回复，并将聊天记录保存到本地数据库中。

本项目是我学习 Python Web 开发过程中的阶段性作品，主要用于练习 Flask 路由、HTML 模板渲染、数据库增删查改、分页、搜索、详情页和 AI API 接入等核心功能。

## 项目功能

目前已实现以下功能：

1. AI 聊天问答
   用户可以在首页输入金融相关问题，系统调用 DeepSeek API 返回 AI 回复。

2. 多轮对话
   当前浏览器会话中支持上下文连续对话，AI 可以根据前文继续回答。

3. 聊天记录保存
   每一次用户提问和 AI 回复都会保存到 SQLite 数据库中。

4. 历史记录页面
   用户可以进入历史记录页面，查看过往聊天内容。

5. 历史记录搜索
   支持通过关键词搜索历史聊天记录，例如搜索“基金”“债券”等内容。

6. 历史记录分页
   历史记录页面支持分页显示，每页展示固定数量的聊天记录，避免一次性显示过多内容。

7. 历史记录详情页
   用户可以点击某一条历史记录，进入单独详情页查看完整问答内容。

8. 删除历史记录
   支持删除单条历史记录，也支持清空全部历史记录。

9. 快捷问题按钮
   首页提供常见金融问题快捷按钮，方便用户快速提问。

10. 基础前端交互
    实现了空输入提示、按钮加载状态、回车发送、自动滚动到底部等基础交互效果。

## 技术栈

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript
* Jinja2 模板语法
* DeepSeek API
* Git / GitHub

## 项目结构

```text
ai-finance-assistant/
├── app.py
├── database.py
├── chat_history.db
├── templates/
│   ├── index.html
│   ├── history.html
│   └── history_detail.html
├── static/
│   └── style.css
├── .env
├── .gitignore
└── README.md
```

## 核心学习内容

通过这个项目，我主要学习和实践了以下内容：

* Flask 路由的基本使用
* GET 请求和 POST 请求的区别
* 表单提交和页面跳转
* `request.form` 获取表单数据
* `request.args.get()` 获取网址参数
* `url_for()` 动态生成链接
* `redirect()` 页面重定向
* Jinja2 模板循环和条件判断
* SQLite 数据库连接、插入、查询、删除
* 使用 `id` 查询单条数据
* 使用 `LIKE` 实现模糊搜索
* 使用 `LIMIT` 和 `OFFSET` 实现分页
* 使用 `COUNT(*)` 统计总记录数
* 使用 session 保存当前对话上下文
* 使用 `.env` 管理 API Key
* 使用 Git 进行版本管理

## 本地运行方式

1. 克隆项目

```bash
git clone 项目地址
cd ai-finance-assistant
```

2. 创建并激活虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
```

3. 安装依赖

```bash
pip install flask openai python-dotenv
```

4. 新建 `.env` 文件

```env
DEEPSEEK_API_KEY=你的API_KEY
FLASK_SECRET_KEY=你的Flask密钥
```

5. 运行项目

```bash
python app.py
```

6. 浏览器访问

```text
http://127.0.0.1:5000
```

## 当前项目状态

项目目前已经完成了一个基础 AI 金融助手 Web 应用的主要功能，包括聊天、记录保存、搜索、分页、详情页和删除功能。整体结构已经具备一个小型 Web 应用的雏形。

后续可以继续扩展更多功能，例如：

* 历史记录详情页删除按钮
* 历史记录导出功能
* 用户登录系统
* 更美观的前端页面
* 流式输出 AI 回复
* 部署到云服务器
* 增加金融知识库检索功能
* 增加更专业的风险测评模块

## 学习收获

通过这个项目，我逐渐理解了 Python Web 应用的基本运行逻辑：

```text
用户在浏览器操作
↓
浏览器发送请求
↓
Flask 根据路由找到对应函数
↓
函数处理表单、网址参数、数据库或 AI 请求
↓
后端把数据传给 HTML 模板
↓
页面渲染并展示给用户
```

这个项目让我从单纯照着代码写，逐渐开始理解 Web 应用中“路由、函数、数据库、模板、页面展示”之间的关系，也让我对后续继续学习 Flask、数据库、前端交互和 AI 应用开发有了更清晰的方向。

# django-personal-blog

一个基于 Django 的个人博客系统，包含文章发布、分类管理、全文搜索、评论、深／浅色主题切换等功能，前端使用 Bootstrap 5 和自定义交互脚本。

---

## 功能特性

* **用户认证**：注册、登录、登出
* **文章管理**：文章的创建、编辑、删除、草稿与发布
* **分类 & 标签**：为文章添加分类、标签，展示分类页面与标签页面
* **全文搜索**：在文章标题与内容中快速搜索
* **评论系统**：基于 Django 模型的文章评论功能
* **响应式布局**：Bootstrap 5 实现手机／平板／桌面友好适配
* **深／浅色主题**：一键切换，记忆用户偏好
* **后台管理**：Django Admin，方便内容审核与用户管理
* **自定义交互**：键盘快捷键、通知弹窗、语音播报（可选）等脚本增强

---

## 技术栈

* **后端**：Python 3.8+ / Django 5.1
* **数据库**：MySQL 9.2（开发 & 生产）
* **前端**：Bootstrap 5 / Vanilla JS (ES6)
* **依赖管理**：`pip` + `requirements.txt`
* **部署**：Gunicorn + Nginx / Docker (可选)
* **可选**：Celery + Redis（异步任务）、Django REST Framework（API 支持）

---

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/code-third-space/django-personal-blog.git
cd django-personal-blog
git checkout dev
```

### 2. 创建并激活虚拟环境

```bash
python3 -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 3. 安装依赖

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. 配置环境变量

在项目根目录新建 `.env`（或复制 `.env.example`），并填写：

```ini
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=mysql://username:password@127.0.0.1:3306/db_name

# 可选：邮件、缓存、第三方服务配置
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
REDIS_URL=redis://localhost:6379/0
```

### 5. 数据库迁移 & 创建超级用户

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. 运行开发服务器

```bash
python manage.py runserver
```

访问 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 即可查看首页；
访问 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) 登录后台管理。

---

## 项目结构

```
django-personal-blog/
├── articles/                   # 文章 app
│   ├── migrations/             # 数据库迁移
│   ├── templates/articles/     # 前端模板
│   ├── static/articles/        # CSS / JS / 图片
│   ├── models.py               # 数据模型：Article, Category, Comment…
│   ├── views.py                # 视图函数 / 类视图
│   ├── urls.py                 # URL 路由
│   └── …                       
├── personal_blog/              # Django 项目配置
│   ├── settings.py             # 全局配置
│   ├── urls.py                 # 顶级 URL 路由
│   ├── asgi.py
│   └── wsgi.py
├── static/                     # 全局静态资源（CSS / JS）
├── templates/                  # 全局模板（base.html, includes…）
├── manage.py                   # Django 管理脚本
├── requirements.txt            # Python 依赖列表
├── .env.example                # 环境变量示例
└── README.md
```

---

## 部署建议

1. **收集静态文件**

   ```bash
   python manage.py collectstatic --noinput
   ```
2. **使用 Gunicorn**（示例）

   ```bash
   gunicorn personal_blog.wsgi:application \
     --bind 0.0.0.0:8000 \
     --workers 4
   ```
3. **反向代理**：Nginx 或 Caddy
4. **安全**：关闭 `DEBUG`，设置合适的 `ALLOWED_HOSTS`，启用 HTTPS

---

## 贡献

1. Fork 本仓库
2. 创建功能分支 `git checkout -b feature/your-feature`
3. 提交改动 `git commit -m "Add new feature"`
4. 推送分支 `git push origin feature/your-feature`
5. 在 GitHub 上发起 Pull Request

---

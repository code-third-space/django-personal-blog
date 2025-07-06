from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from articles.models import Article
import random

class Command(BaseCommand):
    help = "批量为Web开发分类填充8篇真实知识点的文章"

    def handle(self, *args, **kwargs):
        # 获取或创建作者
        author = CustomUser.objects.filter(is_superuser=True).first()
        if not author:
            author = CustomUser.objects.create_superuser(
                username="webadmin",
                email="webadmin@example.com",
                password="webadmin123",
                city="北京",
                phone="13800000000",
                user_type="admin"
            )

        articles = [
            (
                "HTML5新特性详解与应用",
                """HTML5是HTML的最新版本，带来了许多新特性和API，使Web开发更加丰富和强大。

主要新特性：
1. 语义化标签：`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
2. 表单增强：新的input类型（email、date、range等）
3. 多媒体支持：`<video>`和`<audio>`标签
4. Canvas绘图：2D图形绘制
5. Web Storage：localStorage和sessionStorage

示例：
```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML5示例</title>
</head>
<body>
    <header>
        <h1>网站标题</h1>
        <nav>
            <ul>
                <li><a href="#home">首页</a></li>
                <li><a href="#about">关于</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section>
            <article>
                <h2>文章标题</h2>
                <p>文章内容...</p>
            </article>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 版权所有</p>
    </footer>
</body>
</html>
```

HTML5的语义化标签不仅提高了代码的可读性，还有助于SEO和可访问性。
""",
                8  # 前端技术
            ),
            (
                "CSS3高级特性与动画",
                """CSS3引入了许多强大的新特性，包括Flexbox、Grid、动画、渐变等，让Web界面更加美观和交互性强。

核心特性：
1. Flexbox布局：一维布局系统
2. CSS Grid：二维布局系统
3. 动画和过渡：@keyframes和transition
4. 渐变和阴影：linear-gradient、box-shadow
5. 媒体查询：响应式设计

示例：
```css
/* Flexbox布局 */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
}

/* CSS Grid布局 */
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

/* 动画 */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.animated {
    animation: fadeIn 1s ease-in;
}

/* 渐变背景 */
.gradient-bg {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
}

/* 响应式设计 */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }
}
```

掌握CSS3的这些特性，可以创建现代化的Web界面。
""",
                8  # 前端技术
            ),
            (
                "JavaScript ES6+新特性详解",
                """ES6（ES2015）及后续版本为JavaScript带来了许多现代化特性，大大提升了开发效率和代码质量。

主要新特性：
1. 箭头函数：简洁的函数语法
2. 解构赋值：从数组或对象中提取值
3. 模板字符串：支持插值的字符串
4. Promise和async/await：异步编程
5. 类和模块：面向对象编程
6. 扩展运算符：数组和对象的展开

示例：
```javascript
// 箭头函数
const add = (a, b) => a + b;

// 解构赋值
const [first, second] = [1, 2];
const { name, age } = { name: 'Alice', age: 25 };

// 模板字符串
const greeting = `Hello, ${name}! You are ${age} years old.`;

// Promise和async/await
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// 类
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    sayHello() {
        return `Hello, I'm ${this.name}`;
    }
}

// 扩展运算符
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]
```

这些特性让JavaScript更加现代化和易用。
""",
                8  # 前端技术
            ),
            (
                "React框架入门与实践",
                """React是由Facebook开发的前端框架，采用组件化开发模式，是目前最流行的前端框架之一。

核心概念：
1. 组件：可复用的UI单元
2. JSX：JavaScript XML语法
3. 状态管理：useState和useEffect
4. 虚拟DOM：高效的DOM更新机制
5. 生命周期：组件的创建、更新、销毁

示例：
```jsx
import React, { useState, useEffect } from 'react';

function Counter() {
    const [count, setCount] = useState(0);
    
    useEffect(() => {
        document.title = `Count: ${count}`;
    }, [count]);
    
    return (
        <div>
            <h2>计数器: {count}</h2>
            <button onClick={() => setCount(count + 1)}>
                增加
            </button>
            <button onClick={() => setCount(count - 1)}>
                减少
            </button>
        </div>
    );
}

function App() {
    return (
        <div className="App">
            <h1>React应用</h1>
            <Counter />
        </div>
    );
}

export default App;
```

React的组件化开发模式提高了代码的可维护性和复用性。
""",
                8  # 前端技术
            ),
            (
                "Vue.js响应式原理与组件开发",
                """Vue.js是一个渐进式JavaScript框架，具有响应式数据绑定和组件化开发的特点。

核心特性：
1. 响应式数据绑定：数据变化自动更新视图
2. 组件系统：可复用的Vue组件
3. 指令系统：v-if、v-for、v-model等
4. 生命周期钩子：created、mounted、updated等
5. 计算属性和侦听器：computed和watch

示例：
```vue
<template>
    <div id="app">
        <h1>{{ title }}</h1>
        <input v-model="message" placeholder="输入消息">
        <p>{{ message }}</p>
        
        <button @click="increment">点击次数: {{ count }}</button>
        
        <ul>
            <li v-for="item in items" :key="item.id">
                {{ item.name }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'App',
    data() {
        return {
            title: 'Vue.js应用',
            message: '',
            count: 0,
            items: [
                { id: 1, name: '项目1' },
                { id: 2, name: '项目2' }
            ]
        }
    },
    computed: {
        reversedMessage() {
            return this.message.split('').reverse().join('');
        }
    },
    methods: {
        increment() {
            this.count++;
        }
    },
    mounted() {
        console.log('组件已挂载');
    }
}
</script>
```

Vue.js的响应式系统让数据驱动视图变得简单高效。
""",
                8  # 前端技术
            ),
            (
                "Node.js后端开发入门",
                """Node.js是基于Chrome V8引擎的JavaScript运行时，让JavaScript可以在服务器端运行。

核心概念：
1. 事件驱动：非阻塞I/O操作
2. 模块系统：CommonJS和ES模块
3. 包管理：npm和yarn
4. 异步编程：回调、Promise、async/await
5. Express框架：Web应用框架

示例：
```javascript
const express = require('express');
const app = express();
const port = 3000;

// 中间件
app.use(express.json());
app.use(express.static('public'));

// 路由
app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.get('/api/users', async (req, res) => {
    try {
        // 模拟数据库查询
        const users = [
            { id: 1, name: 'Alice' },
            { id: 2, name: 'Bob' }
        ];
        res.json(users);
    } catch (error) {
        res.status(500).json({ error: '服务器错误' });
    }
});

app.post('/api/users', (req, res) => {
    const { name, email } = req.body;
    // 处理用户创建逻辑
    res.status(201).json({ message: '用户创建成功' });
});

// 错误处理中间件
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('服务器错误');
});

app.listen(port, () => {
    console.log(`服务器运行在 http://localhost:${port}`);
});
```

Node.js让JavaScript成为全栈开发语言。
""",
                9  # 后端技术
            ),
            (
                "RESTful API设计原则",
                """RESTful API是一种软件架构风格，用于设计网络应用程序的API接口。

设计原则：
1. 资源导向：使用名词而非动词
2. HTTP方法：GET、POST、PUT、DELETE
3. 状态码：200、201、400、404、500等
4. 无状态：每个请求包含所有必要信息
5. 统一接口：一致的API设计模式

示例：
```javascript
// 用户资源API
// GET /api/users - 获取用户列表
app.get('/api/users', (req, res) => {
    const users = getUsers();
    res.json(users);
});

// GET /api/users/:id - 获取特定用户
app.get('/api/users/:id', (req, res) => {
    const user = getUserById(req.params.id);
    if (user) {
        res.json(user);
    } else {
        res.status(404).json({ error: '用户不存在' });
    }
});

// POST /api/users - 创建新用户
app.post('/api/users', (req, res) => {
    const { name, email } = req.body;
    const newUser = createUser({ name, email });
    res.status(201).json(newUser);
});

// PUT /api/users/:id - 更新用户
app.put('/api/users/:id', (req, res) => {
    const { name, email } = req.body;
    const updatedUser = updateUser(req.params.id, { name, email });
    res.json(updatedUser);
});

// DELETE /api/users/:id - 删除用户
app.delete('/api/users/:id', (req, res) => {
    deleteUser(req.params.id);
    res.status(204).send();
});
```

良好的RESTful API设计提高了系统的可维护性和可扩展性。
""",
                9  # 后端技术
            ),
            (
                "Web安全与最佳实践",
                """Web安全是Web开发中至关重要的环节，涉及多种安全威胁和防护措施。

主要安全威胁：
1. XSS（跨站脚本攻击）：注入恶意脚本
2. CSRF（跨站请求伪造）：伪造用户请求
3. SQL注入：数据库查询注入
4. 身份验证和授权：用户身份验证
5. 数据加密：敏感数据保护

防护措施示例：
```javascript
// XSS防护
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// CSRF防护
app.use(csrf());
app.post('/api/data', (req, res) => {
    // 验证CSRF token
    if (!req.csrfToken()) {
        return res.status(403).json({ error: 'CSRF验证失败' });
    }
    // 处理请求
});

// SQL注入防护（使用参数化查询）
const query = 'SELECT * FROM users WHERE id = ?';
db.query(query, [userId], (err, results) => {
    // 处理结果
});

// 密码加密
const bcrypt = require('bcrypt');
const saltRounds = 10;

async function hashPassword(password) {
    return await bcrypt.hash(password, saltRounds);
}

async function verifyPassword(password, hash) {
    return await bcrypt.compare(password, hash);
}

// HTTPS强制
app.use((req, res, next) => {
    if (req.header('x-forwarded-proto') !== 'https') {
        res.redirect(`https://${req.header('host')}${req.url}`);
    } else {
        next();
    }
});
```

Web安全需要从多个层面进行防护，确保应用的安全性。
""",
                3  # 网络安全
            ),
        ]

        for title, content, subcategory in articles:
            Article.objects.create(
                title=title,
                blog_type=1,  # Web
                subcategory=subcategory,
                country=0,  # 中国
                city=random.randint(0, 15),
                author=author,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                content=content,
            )
        self.stdout.write(self.style.SUCCESS("已为Web开发分类填充8篇真实知识点文章！")) 
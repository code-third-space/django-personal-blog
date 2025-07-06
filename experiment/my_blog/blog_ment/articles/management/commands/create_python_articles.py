from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from articles.models import Article
import random

class Command(BaseCommand):
    help = "批量为Python分类填充8篇真实知识点的文章"

    def handle(self, *args, **kwargs):
        # 获取或创建作者
        author = CustomUser.objects.filter(is_superuser=True).first()
        if not author:
            author = CustomUser.objects.create_superuser(
                username="pyadmin",
                email="pyadmin@example.com",
                password="pyadmin123",
                city="北京",
                phone="13800000000",
                user_type="admin"
            )

        articles = [
            (
                "Python基础语法详解",
                """Python是一门简洁易读的编程语言。其基础语法包括变量定义、数据类型（int、float、str、list、dict等）、流程控制（if、for、while）、函数定义与调用等。

示例：
```python
# 变量与数据类型
a = 10
b = 3.14
name = "Alice"
lst = [1, 2, 3]
d = {"x": 1, "y": 2}

# 流程控制
for i in lst:
    print(i)

if a > 5:
    print("a大于5")

# 函数定义
def add(x, y):
    return x + y

print(add(2, 3))
```
掌握这些基础语法，是学习Python的第一步。
""",
                0
            ),
            (
                "列表推导式与生成器表达式",
                """列表推导式是Python中用于快速生成列表的简洁语法。生成器表达式则用于按需生成数据，节省内存。

示例：
```python
# 列表推导式
squares = [x**2 for x in range(10)]
# 生成器表达式
squares_gen = (x**2 for x in range(10))
```
列表推导式适合一次性生成所有数据，生成器表达式适合处理大数据或流式数据。
""",
                0
            ),
            (
                "装饰器的原理与应用",
                """装饰器是Python中用于增强函数功能的语法糖，本质是高阶函数。

示例：
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("函数开始执行")
        result = func(*args, **kwargs)
        print("函数执行结束")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()
```
装饰器常用于日志、权限校验、缓存等场景。
""",
                0
            ),
            (
                "面向对象编程（OOP）进阶",
                """Python支持面向对象编程，包括类、继承、多态、魔法方法等。

示例：
```python
class Animal:
    def speak(self):
        print("动物叫")

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

d = Dog()
d.speak()  # 输出：汪汪汪
```
掌握OOP有助于构建复杂、可维护的程序结构。
""",
                0
            ),
            (
                "Python中的异步编程：asyncio实战",
                """asyncio是Python用于异步编程的标准库，适合高并发场景。

示例：
```python
import asyncio

async def fetch_data():
    print("开始获取数据")
    await asyncio.sleep(1)
    print("数据获取完毕")
    return 42

async def main():
    result = await fetch_data()
    print(f"结果: {result}")

asyncio.run(main())
```
async/await语法让异步代码更易读写。
""",
                1
            ),
            (
                "常用标准库详解：collections与itertools",
                """collections和itertools是Python中非常实用的标准库。

- `collections` 提供了如`Counter`、`defaultdict`、`deque`等数据结构。
- `itertools` 提供了高效的迭代器工具，如`chain`、`cycle`、`combinations`等。

示例：
```python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
print(Counter(nums))  # Counter({3: 3, 2: 2, 1: 1})

from itertools import combinations
for c in combinations([1,2,3], 2):
    print(c)
```
""",
                2
            ),
            (
                "错误与异常处理机制",
                """Python通过try/except语句处理异常，支持自定义异常类型。

示例：
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"发生错误: {e}")
finally:
    print("无论如何都会执行")
```
可以自定义异常类：
```python
class MyError(Exception):
    pass
```
合理的异常处理能提升程序健壮性。
""",
                3
            ),
            (
                "文件与数据读写实用技巧",
                """Python支持多种文件和数据格式的读写，如文本、二进制、JSON、CSV等。

示例：
```python
# 文本文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, world!')

# 读取
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# JSON
import json
data = {'a': 1, 'b': 2}
with open('data.json', 'w') as f:
    json.dump(data, f)
```
""",
                4
            ),
        ]

        for title, content, subcategory in articles:
            Article.objects.create(
                title=title,
                blog_type=0,  # Python
                subcategory=subcategory,
                country=0,  # 中国
                city=random.randint(0, 15),
                author=author,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                content=content,
            )
        self.stdout.write(self.style.SUCCESS("已为Python分类填充8篇真实知识点文章！")) 
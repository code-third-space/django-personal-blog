from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from articles.models import Article
import random

class Command(BaseCommand):
    help = "批量为后端框架分类填充8篇真实知识点的文章"

    def handle(self, *args, **kwargs):
        # 获取或创建作者
        author = CustomUser.objects.filter(is_superuser=True).first()
        if not author:
            author = CustomUser.objects.create_superuser(
                username="backendadmin",
                email="backendadmin@example.com",
                password="backendadmin123",
                city="北京",
                phone="13800000000",
                user_type="admin"
            )

        articles = [
            (
                "Django框架深度解析",
                "Django是一个高级的Python Web框架, 遵循MVT(Model-View-Template)架构模式, 提供了完整的Web开发解决方案. 核心特性包括ORM(对象关系映射), 管理后台, 表单处理, 中间件, 缓存系统等. Django的'电池包含'理念让开发者可以快速构建功能完整的Web应用.",
                9
            ),
            (
                "Flask轻量级框架实战",
                "Flask是一个轻量级的Python Web框架, 具有高度的灵活性和可扩展性, 适合构建小型到中型应用. 核心特性包括微框架设计, 蓝图系统, Jinja2模板引擎, Werkzeug工具库, 丰富的插件生态. Flask的简洁性让开发者可以专注于业务逻辑, 而不是框架约束.",
                9
            ),
            (
                "微服务架构设计与实践",
                "微服务架构是一种将应用程序拆分为小型, 独立服务的软件架构模式, 每个服务运行在自己的进程中. 核心原则包括单一职责, 独立部署, 技术多样性, 数据隔离, 服务发现. 微服务架构提高了系统的可扩展性和可维护性, 但也增加了复杂性.",
                9
            ),
            (
                "API网关设计与实现",
                "API网关是微服务架构中的核心组件, 负责请求路由, 负载均衡, 认证授权, 限流等功能. 主要功能包括路由转发, 负载均衡, 认证授权, 限流熔断, 日志监控. API网关简化了客户端与微服务的交互, 提供了统一的安全和监控入口.",
                9
            ),
            (
                "数据库连接池与性能优化",
                "数据库连接池是提高数据库访问性能的重要技术, 通过复用数据库连接减少连接建立和销毁的开销. 核心概念包括连接复用, 连接管理, 负载均衡, 故障恢复, 监控统计. 连接池技术显著提高了数据库访问性能, 特别是在高并发场景下.",
                4
            ),
            (
                "缓存策略与Redis实战",
                "缓存是提高系统性能的重要手段, Redis作为高性能的内存数据库, 广泛应用于缓存场景. 缓存策略包括缓存穿透, 缓存击穿, 缓存雪崩, 缓存更新, 缓存预热. Redis缓存技术显著提升了系统响应速度, 减少了数据库压力.",
                4
            ),
            (
                "消息队列与异步处理",
                "消息队列是分布式系统中实现异步处理, 解耦服务的重要组件, 支持高并发和可靠性保证. 核心概念包括生产者-消费者模式, 消息持久化, 消息确认机制, 死信队列, 消息优先级. 消息队列实现了系统解耦, 提高了系统的可靠性和可扩展性.",
                9
            ),
            (
                "负载均衡与高可用架构",
                "负载均衡是分布式系统中的关键技术, 通过分发请求到多个服务器实例, 提高系统性能和可用性. 负载均衡策略包括轮询(Round Robin), 加权轮询, 最少连接, IP哈希, 响应时间. 负载均衡技术提高了系统的性能和可用性, 是现代分布式系统的核心组件.",
                4
            ),
        ]

        for title, content, subcategory in articles:
            Article.objects.create(
                title=title,
                blog_type=2,  # Backend
                subcategory=subcategory,
                country=0,  # 中国
                city=random.randint(0, 15),
                author=author,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                content=content,
            )
        self.stdout.write(self.style.SUCCESS("已为后端框架分类填充8篇真实知识点文章!")) 
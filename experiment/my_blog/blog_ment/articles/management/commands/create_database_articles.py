from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from articles.models import Article
import random

class Command(BaseCommand):
    help = "批量为数据库分类填充8篇真实知识点的文章"

    def handle(self, *args, **kwargs):
        # 获取或创建作者
        author = CustomUser.objects.filter(is_superuser=True).first()
        if not author:
            author = CustomUser.objects.create_superuser(
                username="dbadmin",
                email="dbadmin@example.com",
                password="dbadmin123",
                city="北京",
                phone="13800000000",
                user_type="admin"
            )

        articles = [
            (
                "MySQL数据库优化实战",
                "MySQL是最流行的关系型数据库之一, 性能优化是数据库管理的核心技能. 主要优化策略包括索引优化, 查询优化, 配置调优, 分区表设计, 读写分离等. 通过合理的索引设计, 可以显著提升查询性能; 通过查询优化, 减少不必要的全表扫描; 通过配置调优, 充分利用服务器资源. 数据库优化需要结合具体业务场景, 进行系统性的分析和改进.",
                3
            ),
            (
                "PostgreSQL高级特性详解",
                "PostgreSQL是一个功能强大的开源关系型数据库, 支持多种高级特性. 核心特性包括JSON数据类型支持, 全文搜索, 地理信息处理, 存储过程, 触发器, 视图等. PostgreSQL的JSON支持让开发者可以灵活存储半结构化数据; 全文搜索功能提供强大的文本检索能力; 地理信息处理支持空间数据查询. 这些特性使PostgreSQL成为企业级应用的首选数据库.",
                3
            ),
            (
                "MongoDB NoSQL数据库实践",
                "MongoDB是一个基于文档的NoSQL数据库, 具有高度的灵活性和可扩展性. 主要特点包括文档存储, 动态模式, 水平扩展, 聚合管道, 地理空间索引等. MongoDB的文档存储模式适合存储复杂的嵌套数据结构; 动态模式允许不同文档有不同的字段; 水平扩展能力支持大数据量处理. MongoDB特别适合处理非结构化或半结构化数据, 是现代Web应用的重要选择.",
                2
            ),
            (
                "Redis内存数据库应用",
                "Redis是一个高性能的内存数据库, 支持多种数据结构. 核心功能包括字符串, 哈希, 列表, 集合, 有序集合等数据类型; 支持持久化, 主从复制, 哨兵模式, 集群模式等. Redis的高性能特性使其成为缓存, 会话存储, 消息队列的理想选择. 通过合理使用Redis, 可以显著提升系统响应速度, 减少数据库压力.",
                2
            ),
            (
                "数据库设计范式与反范式",
                "数据库设计范式是关系型数据库设计的基础理论, 包括第一范式(1NF), 第二范式(2NF), 第三范式(3NF), BCNF等. 范式化设计可以减少数据冗余, 保证数据一致性, 但可能影响查询性能. 反范式化设计通过适当的数据冗余来提升查询性能, 但需要权衡数据一致性. 在实际项目中, 需要根据业务需求选择合适的范式级别.",
                2
            ),
            (
                "数据库事务与ACID特性",
                "数据库事务是保证数据一致性的重要机制, ACID特性包括原子性(Atomicity), 一致性(Consistency), 隔离性(Isolation), 持久性(Durability). 事务的隔离级别包括读未提交, 读已提交, 可重复读, 串行化等. 不同隔离级别在性能和一致性之间有不同的权衡. 理解事务机制对于开发可靠的数据库应用至关重要.",
                2
            ),
            (
                "数据库索引设计与优化",
                "索引是提升数据库查询性能的关键技术, 包括B树索引, 哈希索引, 全文索引, 复合索引等. 合理的索引设计可以显著提升查询速度, 但过多的索引会影响写入性能. 索引优化策略包括选择性分析, 覆盖索引, 索引合并等. 通过分析查询执行计划, 可以识别索引使用情况并进行优化.",
                2
            ),
            (
                "数据库备份与恢复策略",
                "数据库备份与恢复是数据安全的重要保障, 包括全量备份, 增量备份, 差异备份等策略. 备份方式包括物理备份和逻辑备份, 各有优缺点. 恢复策略需要考虑RTO(恢复时间目标)和RPO(恢复点目标). 通过制定完善的备份恢复计划, 可以最大程度减少数据丢失风险.",
                2
            ),
        ]

        for title, content, subcategory in articles:
            Article.objects.create(
                title=title,
                blog_type=3,  # Database
                subcategory=subcategory,
                country=0,  # 中国
                city=random.randint(0, 15),
                author=author,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                content=content,
            )
        self.stdout.write(self.style.SUCCESS("已为数据库分类填充8篇真实知识点文章!")) 
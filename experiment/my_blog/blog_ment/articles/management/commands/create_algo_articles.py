from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from articles.models import Article
import random

class Command(BaseCommand):
    help = "批量为算法与数据结构分类填充8篇真实知识点的文章"

    def handle(self, *args, **kwargs):
        # 获取或创建作者
        author = CustomUser.objects.filter(is_superuser=True).first()
        if not author:
            author = CustomUser.objects.create_superuser(
                username="algoadmin",
                email="algoadmin@example.com",
                password="algoadmin123",
                city="北京",
                phone="13800000000",
                user_type="admin"
            )

        articles = [
            (
                "排序算法详解与实现",
                "排序算法是计算机科学的基础算法, 包括冒泡排序, 选择排序, 插入排序, 快速排序, 归并排序, 堆排序等. 不同排序算法在时间复杂度, 空间复杂度, 稳定性方面各有特点. 快速排序平均时间复杂度为O(nlogn), 是最常用的排序算法; 归并排序是稳定的排序算法, 时间复杂度为O(nlogn); 堆排序适合处理大数据量的排序. 选择合适的排序算法需要根据具体应用场景和性能要求.",
                1
            ),
            (
                "搜索算法与优化策略",
                "搜索算法包括线性搜索, 二分搜索, 深度优先搜索(DFS), 广度优先搜索(BFS), A*算法等. 二分搜索适用于有序数组, 时间复杂度为O(logn); DFS适合解决回溯问题, 如八皇后, 数独等; BFS适合寻找最短路径, 如迷宫寻路; A*算法是启发式搜索, 结合了Dijkstra算法和贪心策略. 搜索算法的选择取决于问题特性和性能要求.",
                1
            ),
            (
                "数据结构基础与应用",
                "数据结构是算法的基础, 包括数组, 链表, 栈, 队列, 树, 图等. 数组支持随机访问, 但插入删除效率低; 链表插入删除效率高, 但不支持随机访问; 栈和队列是线性数据结构, 分别遵循LIFO和FIFO原则; 树结构包括二叉树, 二叉搜索树, 平衡树等; 图结构用于表示复杂的关系网络. 合理选择数据结构可以显著提升算法效率.",
                2
            ),
            (
                "动态规划算法实战",
                "动态规划是解决复杂问题的有效方法, 通过将问题分解为子问题来求解. 经典问题包括斐波那契数列, 背包问题, 最长公共子序列, 编辑距离, 矩阵链乘法等. 动态规划的核心是状态定义和状态转移方程. 通过记忆化搜索或自底向上的方式实现, 可以避免重复计算. 动态规划在字符串处理, 图论, 优化问题中有广泛应用.",
                2
            ),
            (
                "贪心算法与局部最优",
                "贪心算法通过每一步选择局部最优解来构建全局解, 虽然不一定得到全局最优解, 但通常能得到较好的近似解. 经典应用包括活动选择问题, 霍夫曼编码, 最小生成树算法(Kruskal, Prim), 单源最短路径(Dijkstra算法)等. 贪心算法的关键是证明贪心选择性质, 即局部最优选择能导致全局最优解. 在实际应用中, 贪心算法通常简单高效.",
                2
            ),
            (
                "图论算法与网络分析",
                "图论算法处理节点和边的关系, 包括图的遍历, 最短路径, 最小生成树, 网络流等. 图的表示方法包括邻接矩阵和邻接表; 遍历算法包括DFS和BFS; 最短路径算法包括Dijkstra, Floyd-Warshall等; 最小生成树算法包括Kruskal和Prim; 网络流算法用于解决最大流问题. 图论算法在社交网络分析, 路由算法, 生物信息学等领域有重要应用.",
                2
            ),
            (
                "字符串算法与模式匹配",
                "字符串算法处理文本数据, 包括字符串匹配, 编辑距离, 最长公共子序列, 回文串检测等. KMP算法是高效的字符串匹配算法, 时间复杂度为O(m+n); Boyer-Moore算法是另一种高效的匹配算法; 编辑距离算法用于计算两个字符串的相似度; 回文串检测算法包括中心扩展法和Manacher算法. 字符串算法在文本处理, 生物信息学, 自然语言处理中有广泛应用.",
                2
            ),
            (
                "高级数据结构详解",
                "高级数据结构包括红黑树, B树, 跳表, 并查集, 线段树等. 红黑树是自平衡的二叉搜索树, 插入删除时间复杂度为O(logn); B树是多路搜索树, 适合磁盘存储; 跳表是链表的多层结构, 提供对数时间复杂度的查找; 并查集用于处理集合的合并和查询; 线段树用于处理区间查询和更新. 这些数据结构在数据库, 文件系统, 算法竞赛中有重要应用.",
                2
            ),
        ]

        for title, content, subcategory in articles:
            Article.objects.create(
                title=title,
                blog_type=4,  # Algo
                subcategory=subcategory,
                country=0,  # 中国
                city=random.randint(0, 15),
                author=author,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                content=content,
            )
        self.stdout.write(self.style.SUCCESS("已为算法与数据结构分类填充8篇真实知识点文章!")) 
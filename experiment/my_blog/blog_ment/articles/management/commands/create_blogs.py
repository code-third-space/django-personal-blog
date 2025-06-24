from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from articles.models import Article, get_subcategories
import random
from datetime import datetime

User = get_user_model()

class Command(BaseCommand):
    help = '为每个主分类创建10篇博客文章'

    def handle(self, *args, **kwargs):
        # 获取或创建测试用户
        test_user, created = User.objects.get_or_create(
            username='test_user',
            defaults={
                'email': 'test@example.com',
                'is_staff': True
            }
        )
        if created:
            test_user.set_password('test123456')
            test_user.save()

        # 为每个主分类创建10篇博客
        for blog_type in range(6):  # 0-5 对应6个主分类
            self.stdout.write(f'开始创建 {blog_type} 类型的博客...')
            
            # 获取该主分类下的二级分类
            subcategories = get_subcategories(blog_type)
            
            for i in range(10):  # 每个主分类创建10篇
                # 随机选择二级分类
                subcategory = random.choice(subcategories)[0]
                
                # 随机选择城市和国家
                city = random.randint(0, 15)  # 0-15
                country = random.randint(0, 2)  # 0-2
                
                # 创建博客
                blog = Article.objects.create(
                    title=f'测试博客 {blog_type}-{i+1}',
                    blog_type=blog_type,
                    subcategory=subcategory,
                    country=country,
                    city=city,
                    author=test_user,
                    content=f'这是{blog_type}类型的第{i+1}篇测试博客的内容。\n'
                           f'包含了一些测试文本，用于展示博客的基本功能。\n'
                           f'这篇博客属于二级分类：{subcategory}。',
                    content_middle=f'这是中间部分的内容，用于测试分段显示。\n'
                                 f'可以包含更多的测试文本。',
                    content_bottom=f'这是底部部分的内容，用于测试分段显示。\n'
                                 f'可以包含更多的测试文本。',
                )
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'成功创建博客: {blog.title} (类型: {blog_type}, 二级分类: {subcategory})'
                    )
                )

        self.stdout.write(self.style.SUCCESS('所有博客创建完成！')) 
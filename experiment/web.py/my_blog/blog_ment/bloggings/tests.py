from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Me_blog, Category, Tag
from django.core.files.uploadedfile import SimpleUploadedFile

class BloggingsTests(TestCase):
    def setUp(self):
        # 创建测试用户
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # 创建测试分类
        self.category = Category.objects.create(name='测试分类')
        
        # 创建测试标签
        self.tag = Tag.objects.create(name='测试标签')
        
        # 创建测试博客
        self.blog = Me_blog.objects.create(
            blog_title='测试博客',
            blog_type=0,  # 技术类型
            blog_countries=0,
            blog_city=0,
            creator=self.user,
            blog_detail_one='测试内容',
            category=self.category
        )
        self.blog.tags.add(self.tag)
        
        # 创建测试客户端
        self.client = Client()

    def test_blog_display_view(self):
        """测试博客展示页面"""
        response = self.client.get(reverse('bloggings:blog_display'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloggings/blog_display.html')
        self.assertIn('blog_list', response.context)

    def test_blog_detail_view(self):
        """测试博客详情页面"""
        response = self.client.get(
            reverse('bloggings:blog_detail', args=[self.blog.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloggings/blog_detail.html')
        self.assertEqual(response.context['blog'], self.blog)

    def test_blog_search(self):
        """测试博客搜索功能"""
        response = self.client.get(
            reverse('bloggings:blog_search'), 
            {'q': '测试博客'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bloggings/blog_search.html')
        self.assertIn('测试博客', str(response.content))

    def test_blog_category_views(self):
        """测试各个分类页面"""
        categories = [
            'blog_tech',
            'blog_finance',
            'blog_read',
            'blog_scenery',
            'blog_products',
            'blog_current'
        ]
        for category in categories:
            response = self.client.get(reverse(f'bloggings:{category}'))
            self.assertEqual(response.status_code, 200)

    def test_blog_model(self):
        """测试博客模型"""
        blog = Me_blog.objects.get(blog_title='测试博客')
        self.assertEqual(blog.blog_type, 0)
        self.assertEqual(blog.creator, self.user)
        self.assertEqual(blog.category, self.category)
        self.assertTrue(self.tag in blog.tags.all())

    def test_blog_creation(self):
        """测试创建博客"""
        self.client.login(username='testuser', password='testpass123')
        new_blog_data = {
            'blog_title': '新测试博客',
            'blog_type': 1,
            'blog_countries': 0,
            'blog_city': 0,
            'blog_detail_one': '新测试内容',
            'category': self.category.id
        }
        response = self.client.post(reverse('bloggings:blog_add'), new_blog_data)
        self.assertEqual(Me_blog.objects.count(), 2)

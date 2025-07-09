#!/usr/bin/env python
"""
简单的搜索测试脚本
"""
import os
import sys
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings.local')
django.setup()

from articles.models import Article
from django.db.models import Q

def test_search():
    print("=== 搜索功能测试 ===")
    
    # 1. 检查总文章数
    total_articles = Article.objects.count()
    print(f"总文章数: {total_articles}")
    
    # 2. 测试Python搜索
    search_query = "python"
    print(f"\n搜索关键词: '{search_query}'")
    
    # 模拟搜索逻辑
    keywords = search_query.split()
    search_conditions = Q()
    
    for keyword in keywords:
        search_conditions |= (
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword)
        )
    
    results = Article.objects.filter(search_conditions)
    print(f"找到 {results.count()} 篇文章")
    
    # 3. 显示搜索结果
    for i, article in enumerate(results[:5], 1):
        print(f"{i}. {article.title}")
        print(f"   分类: {article.get_blog_type_display()}")
        print(f"   创建时间: {article.created_at}")
        print()
    
    # 4. 测试大小写敏感性
    print("\n=== 大小写测试 ===")
    for test_query in ["python", "Python", "PYTHON"]:
        count = Article.objects.filter(
            Q(title__icontains=test_query) | Q(content__icontains=test_query)
        ).count()
        print(f"'{test_query}': {count} 篇文章")
    
    # 5. 检查具体的Python文章
    print("\n=== Python相关文章 ===")
    python_articles = Article.objects.filter(
        Q(title__icontains="python") | Q(content__icontains="python")
    )
    
    for article in python_articles:
        print(f"标题: {article.title}")
        print(f"内容片段: {article.content[:100] if article.content else '无内容'}...")
        print(f"分类: {article.get_blog_type_display()}")
        print("-" * 50)

if __name__ == "__main__":
    test_search()
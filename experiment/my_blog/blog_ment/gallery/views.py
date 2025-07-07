# gallery/views.py
from django.shortcuts import render, get_object_or_404
from articles.models import Article
import requests, os
from urllib.parse import quote
from django.templatetags.static import static
from deep_translator import GoogleTranslator  # 新增

def article_with_images(request, blog_id):
    # 1) 拿到文章
    blog = get_object_or_404(Article, pk=blog_id)

    # 2) 直接使用原文
    query = blog.title

    # 3) PIXABAY API Key
    API_KEY = os.getenv('PIXABAY_API_KEY')
    if not API_KEY:
        raise RuntimeError("环境变量 PIXABAY_API_KEY 未设置！")

    # 4) per_page>=3
    per_page = 3
    url = (
        "https://pixabay.com/api/"
        f"?key={API_KEY}"
        f"&q={quote(query)}"
        f"&image_type=photo"
        f"&per_page={per_page}"
    )

    # 5) 请求并取第一张
    image = None
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            hits = resp.json().get('hits', [])
            if hits:
                image = hits[0].get('webformatURL')
        else:
            print(f"[gallery] Pixabay 返回状态：{resp.status_code}, 内容：{resp.text}")
    except Exception as e:
        print(f"[gallery] Pixabay 请求失败: {e}")

    if not image:
        image = static('images/default.jpg')

    # 6) 渲染模板
    return render(request, 'articles/blog_detail.html', {
        'blog':  blog,
        'image': image,
    })

import requests, os
from urllib.parse import quote
from django.templatetags.static import static
from functools import lru_cache

@lru_cache(maxsize=128)
def get_pixabay_image(query):
    API_KEY = os.getenv('PIXABAY_API_KEY')
    if not API_KEY:
        return static('images/default.jpg')
    url = (
        "https://pixabay.com/api/"
        f"?key={API_KEY}"
        f"&q={quote(query)}"
        f"&image_type=photo"
        f"&per_page=1"
    )
    try:
        resp = requests.get(url, timeout=3)
        if resp.status_code == 200:
            hits = resp.json().get('hits', [])
            if hits:
                return hits[0].get('webformatURL')
    except Exception as e:
        print(f"[Pixabay] 请求失败: {e}")
    return static('images/default.jpg') 
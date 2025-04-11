"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext as _

from bloggings.models import Me_blog
# 修改导入的用户模型
from accounts.models import CustomUser  # 替换原来的 User 导入
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser  # 修改为 CustomUser
        fields = ['url', 'username', 'email', 'is_staff', 'phone']  # 添加自定义字段

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()  # 修改为 CustomUser
    serializer_class = UserSerializer

class Me_blogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Me_blog
        fields = '__all__'

class Me_blogViewSet(viewsets.ModelViewSet):
    queryset = Me_blog.objects.all()    
    serializer_class = Me_blogSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"bloggings", Me_blogViewSet)


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include("bloggings.urls")),

    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace='rest_framework')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)


admin.site.site_header = _("个人博客")
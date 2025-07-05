from django.contrib.auth import logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)   #调用django的logout（）函数来注销用户
    return redirect('articles:home')  #重定向到命名url articles：name 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

def register_view(request):
    """
    用户注册视图
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '注册成功！')
            return redirect('bloggings:home')  # 替换为您的主页URL名称
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """
    用户登录视图
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '登录成功！')
            return redirect('bloggings:home')
        else:
            messages.error(request, '用户名或密码错误！')
    return render(request, 'accounts/login.html')

def logout_view(request):
    """
    用户注销视图
    """
    logout(request)
    messages.success(request, '您已成功注销！')
    return redirect('bloggings:home')  # 替换为您的主页URL名称

@login_required
def profile_view(request):
    """
    用户个人资料视图
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '个人资料已更新！')
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

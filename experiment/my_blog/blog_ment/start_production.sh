#!/bin/bash

# 生产环境 Django 启动脚本
# 注意：生产环境需要手动设置数据库环境变量

# 设置 Django 环境变量 - 使用生产环境配置
export DJANGO_SETTINGS_MODULE=blog_project.settings.production

echo "=========================================="
echo "生产环境 Django 服务器启动脚本"
echo "=========================================="
echo ""
echo "⚠️  重要提示："
echo "1. 请确保已设置生产环境数据库变量："
echo "   export DB_NAME=your_production_db"
echo "   export DB_USER=your_production_user"
echo "   export DB_PASSWORD=your_production_password"
echo "   export DB_HOST=your_production_host"
echo ""
echo "2. 当前使用的配置: blog_project.settings.production"
echo "3. DEBUG 模式: 关闭"
echo "4. HTTPS 重定向: 启用"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "=========================================="

# 检查必要的环境变量
if [ -z "$DB_NAME" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ]; then
    echo "❌ 错误：请先设置生产环境数据库变量！"
    echo "示例："
    echo "export DB_NAME=your_db_name"
    echo "export DB_USER=your_db_user"
    echo "export DB_PASSWORD=your_db_password"
    echo "export DB_HOST=your_db_host"
    exit 1
fi

echo "✅ 数据库配置检查通过"
echo "数据库: $DB_HOST/$DB_NAME"
echo "用户: $DB_USER"
echo ""

# 启动 Django 生产服务器
echo "🚀 启动生产环境服务器..."
python3 manage.py runserver 0.0.0.0:8000 
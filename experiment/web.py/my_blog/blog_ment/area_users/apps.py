from django.apps import AppConfig


class AreaUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'area_users'
    verbose_name = '用户管理'

    def ready(self):
        import  area_users.signals # 导入信号

from django.contrib import admin
from django.apps import apps, AppConfig

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

class UniversalManageApp(AppConfig):
    name = 'meet_project'

    def ready(self):
        models = apps.get_app_config('running').get_models()
        for model in models:
            admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin),{})
            try:
                admin.site.register(model, admin_class)
            except admin.site.AlreadyRegistered:
                pass
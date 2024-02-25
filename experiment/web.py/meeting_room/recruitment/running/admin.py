from django.contrib import admin
from .models import City, Province, Country

# Register your models here.


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []
    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
                [field.name for field in obj._meta.fields] + \
                [field.name for field in obj._meta.many_to_many]
    
    def get_list_display(self,request):
        return [field.name for field in self.model._meta.concrete_fields]
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


# @admin.register(Country)
# class CountryAdmin(ReadOnlyAdmin):
#     search_fields = ('chn_name', 'eng_name')

# @admin.register(Province)
# class ProvinceAdmin(ReadOnlyAdmin):
#     search_fields = ('conutry_id', 'chn_name', 'eng_name',)

# class CityAdmin(ReadOnlyAdmin):
#     list_display = ('province_id',)
#     autocomplete_fields = ('province_id',)

# admin.site.register(City, CityAdmin)
    
# class AdminClass(admin.ModelAdmin):
#     def __init__(self, model, admin_site):
#         self.list_display = [field.name for field in model._meta.fields]
#         super(AdminClass, self).__init__(model, admin_site)
    
# from django.apps import apps

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model, AdminClass)
#     except admin.site.AlreadyRegistered:
#         pass
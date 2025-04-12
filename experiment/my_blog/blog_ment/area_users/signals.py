from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Area_User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """当创建新用户时，自动创建对应的Area_User记录"""
    if created:
        Area_User.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """当保存用户时，确保Area_User记录也被保存"""
    # 如果用户已有area_profile，则保存它
    try:
        if hasattr(instance, 'area_profile'):
            instance.area_profile.save()
    except Area_User.DoesNotExist:
        # 如果用户没有area_profile，则创建一个
        Area_User.objects.create(user=instance)
        
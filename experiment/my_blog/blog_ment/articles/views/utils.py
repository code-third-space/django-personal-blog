from django.core.mail import send_mail
from django.conf import settings


def send_blog_creation_email(user_email, blog_title):
    subject = f"your blog '{blog_title}' has been created"
    message = f"Hello, \n\nyour blog titled '{blog_title}' has been successfully created on our platform. Thank you"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list) 
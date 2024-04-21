import csv

from django.core.management import BaseCommand
from area_users.models import Area_User

class Command(BaseCommand):
    help = "从一个csv文件的内容中读取博客列表，导入数据中"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='utf8') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                blogusers = Area_User.objects.create(
                    username = row[0],
                    city = row[1],
                    user_remark = row[2],
                )
                print(blogusers)
import datetime
from django.utils import timezone

from django.db import models

# https://docs.djangoproject.com/zh-hans/2.0/ref/models/relations/
# https://docs.djangoproject.com/zh-hans/2.0/topics/db/queries/#field-lookups-intro
# https://docs.djangoproject.com/zh-hans/2.0/topics/db/queries/

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # 后台展示这个字段的一些优化，包括排序及说明
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

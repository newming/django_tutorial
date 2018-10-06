from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.TabularInline 以表格形式显示，占据空间小
# admin.StackedInline 多个块，占据空间大
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # 默认三个 choice


class QuestionAdmin(admin.ModelAdmin):
    # 后台展示的字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 决定了后台管理系统中各个字段显示的顺序
    fieldsets = [
        ('Question info', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # 过滤的一些操作 对应 /admin/polls/question/ 中 右侧 过滤选项卡
    list_filter = ['pub_date']
    # 搜索栏
    search_fields = ['question_text']
    # 每页显示数量
    list_per_page = 5

admin.site.register(Question, QuestionAdmin)

# 将修改添加 choice 的内联到 Question 中
# admin.site.register(Choice)

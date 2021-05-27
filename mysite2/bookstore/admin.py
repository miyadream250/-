from django.contrib import admin

from bookstore.models import Book


class BookManager(admin.ModelAdmin):
    # list_display是固定的写法变量，不能随意改，不同的类属性，关联不同的样式
    list_display = ["id", "title", "pub", "price", "market_price", "is_delete"]

    # 控制字段，哪些可以连接到修改页面
    list_display_links = ["id", "title"]

    """
    常规模型类属性：
    """


# 把我们的模型类注册到admin后台
admin.site.register(Book, BookManager)

"""
python manage.py createsuperuser

登录管理后台
127.0.0.1:8000/admin


增加用户、组
"""

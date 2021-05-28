from django.contrib import admin

from bookstore.models import Book, Author


class BookManager(admin.ModelAdmin):
    """
    常规模型类属性：
    """
    # list_display是固定的写法变量，不能随意改，不同的类属性，关联不同的样式
    list_display = ["id", "title", "pub", "price", "market_price", "is_delete"]

    # 控制字段，哪些可以连接到修改页面，字段必须要在list_display里面
    list_display_links = ["id", "title"]

    # 过滤器，以出版社名称过滤
    list_filter = ["pub", "title"]

    # 搜索框，用书名进行模糊搜索
    search_fields = ["title", "pub"]

    # 添加可编辑的字段，一定是要在显示出来的，和list_display_links里面的字段互斥
    list_editable = ["price", "market_price"]


class AuthorManager(admin.ModelAdmin):
    list_display = ["id", "name", "age", "email"]
    list_editable = ["age"]


# 把我们的模型类注册到admin后台
admin.site.register(Book, BookManager)

admin.site.register(Author, AuthorManager)

"""
python manage.py createsuperuser

登录管理后台
127.0.0.1:8000/admin
增加用户、组


创建自定义的后台管理类，继承admin.ModelAdmin
admin.site.register(Book,后台管理类)
"""

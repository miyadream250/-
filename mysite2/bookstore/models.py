from django.db import models


class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='', unique=True)
    price = models.DecimalField("价格", max_digits=7, decimal_places=2, default=0.0)
    info = models.CharField("描述", max_length=100, default="")
    pub = models.CharField("出版社", max_length=100, default="")
    market_price = models.DecimalField("市场价格", max_digits=7, decimal_places=2, default=0.0)
    grade = models.CharField("年级", max_length=10, default="")
    is_delete = models.BooleanField("是否删除", default=False)

    def __str__(self):
        return "%s_%s_%s_%s" % (self.title, self.price, self.pub, self.market_price)

    class Meta:
        # 修改表名
        db_table = "book"


class Author(models.Model):
    # null = False,默认非空
    name = models.CharField("姓名", max_length=11, default="")
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

    class Meta:
        db_table = "author"


"""

QuerySet是一个model 类对应的实例集合， 即数据库对应表的子集,可以称为查询集。 
首先，QuerySet是可以迭代的对象，然后可以使用python的切片方法进行切片操作，返回的依旧是一个QuerySets的对象。


orm:数据库的引擎
新建表
class Table_name(models.Model):
    field1 = models.CharField(option)
    field2 = models.DecimalField(option)
    field3 = models.IntegerField(option)
    field4 = models.EmailField(option)
    
python manage.py makemigrations 创建迁移文件
python manage.py migrate 执行迁移文件

CRUD  create  read  update delete
进入shell终端，进行调试。
cd 到 工程目录下的manage.py的同层级目录下，敲命令 python manage.py shell

方法一：
insert数据方法：
Table_name.objects.create(field1=xxx,field2=xxx....)

方法二：
table=Table_name()
table.field1=xxxx
table.save()

方法三：
table = Table_name(field1=xxx,field2=xxx)
table.save()

_____________________________________________________________________________________________________
_____________________________________________________________________________________________________
_____________________________________________________________________________________________________
_____________________________________________________________________________________________________

Read数据的方法：
table = Table_name.objects.all()
等价：select * from table_name;

table是一个queryDict对象。
for info in table:
    print(info)
    
重写 类的__str__的魔法方法
def __str__(self):
    return  "%s_%s_%s_%s"%(self.field1,self.field2,self.field3,self.field4)
    

table = Table_name.objects.values_list(“field1”,“field2”)
==>   <QuerySet [('王老师', 28), ('吕老师', 31), ('祁老师', 30)]>
等价：select field1,field2 from Table_name;


table =Table_name.objects.values(“field1”,“field2”)
<QuerySet [{'id': 1, 'name': '王老师', 'age': 28, 'email': 'wangweichao@tedu.cn'}]>
等价：select field1,field2 from Table_name;

——————————————————————————————————————————————————————————————————————————————————————————————————————————
——————————————————————————————————————————————————————————————————————————————————————————————————————————
谓词查找：
table = Table_name.objects.exclude(field1=xxx,field2=xxx)  不包含
==>QuerySet
等价：select *  from Table_name where field1 != xxx and field2!=xxx;



table = Table_name.objects.filter(filed1__exact=xxx) 精确查找filed1=xxx的数据。
==>返回QuerySet
等价：select *  from Table_name where filed1=xxx;

table = Table_name.objects.filter(filed1=xxx);
==>返回QuerySet
等价：select *  from Table_name  where filed1=xxx;
filter(field1__lt=xxx) ==>等价：select *  from Table_name where  field1<xxx;
filter(field1__gt=xxx) ==>等价：select *  from Table_name where  field1>xxx;
filter(field1__lte=xxx)==>等价：select *  from Table_name where  field1<=xxx;
filter(field1__gte=xxx)==>等价：select *  from Table_name where  field1>=xxx;
filter(field1__in=[1,2,6])==>等价：select *  from Table_name where  field1 in (1,2,6);
filter(field1__exact=xxx)==>等价：select *  from Table_name where  field1=xxx;
filter(field1__contains=xxx)==>等价：select *  from Table_name where  field1 like "%xxx%";
filter(field1__range=(values1,values2)) ==>等价：select *  from Table_name where  field1  between values1 and values2;
filter(field1__startswith=xxx)==>等价：select *  from Table_name where  field1 like "xxx%";
filter(field1__endswith=xxx)==>等价：select *  from Table_name where  field1 like "%xxx";

混合使用
Comment.objects.filter(pub_date__year=2015).exclude(pub_date__month=1).exclude(n_visits__exact=0)


table= Table_name.objects.get(filed1 = xxx)  查找filed1=xxx的object对象。有且仅有一条filed1=xxx的数据。多一条或者没有都会报错
 
多的提示：MultipleObjectsReturned错误
没有提示：DoesNotExist

有且只有一条：===>objects，精准的对象
<Book: python_10.63_清华大学出版社_63.98>



Update 更新：
多条更新：
Query_set = Table_name.objects.all().update(filed1=xxx)
==> update  Table_name set filed1=xxx;

单条更新：
obj = Table_name.objects.get(id=xxx)
obj.price=xxx
obj.save()

Delete 删除：
单条删除：
obj= Book.objects.get(id=xxx)
obj.delete()

多条删除：
Query_set =Book.objects.all().delete()
==> delete *  from book_table;
Query_set = Book.objects.filter(id__exact=1).delete()
==>delete *  from book_table where id=1;



______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________



from django.db.models import F,Q


获取兑现自己的price >market_price的对象
Table_name.objects.filter(price__gt=F("market_price"))

对所有的对象price+10
Table_name.objects.filter(price__exact=F("price")+10)

F是ORM对象用来获取对象的字段信息。不直接取这个字段的值，再做SQL转换的时候，再取值信息

Q：
或与非 的 条件查询
|或：价格大于20 【或】  出版社为 “清华大学出版社"
Table_name.objects.filter(Q(price__gt=20)|Q(pub="清华大学出版社"))

& 与：价格小于20 【且】 出版社为 “清华大学出版社"
Table_name.objects.filter(Q(price__lt=20) & Q(pub="清华大学出版社"))


~ 非，&~ 与非
价格小于20   【且】出版社【不，非】为 “清华大学出版社"
Table_name.objects.filter(Q(price__lt=20)&~Q(pub="清华大学出版社"))


【整表聚合函数的使用：】
aggregate:聚和
 from django.db.models import *
 Sum  Avg  Count Max Min 
 
 Book.objects.aggregate(res=Sum("price"))
 ==> select sum(price) from book;
 返回值：{'res': Decimal('110.00')} 
 
【分组聚和的使用方法：】

 test

"""

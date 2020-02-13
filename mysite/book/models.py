from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    """
    分类表
    """
    name = models.CharField(max_length=25, verbose_name='分类名称')
    create_at = models.DateTimeField(auto_now_add=True)  # 创建时间 默认为当前时间

    class Meta:
        verbose_name = "分类管理"  # 设置模型的别名
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)  # 设置排序的字段

    def __str__(self):  # 定义在下拉列表中的显示的名字
        return self.name


class Book(models.Model):
    """
    书籍表
    """
    name = models.CharField(max_length=25, verbose_name='书名')
    description = RichTextField(verbose_name='图书描述')
    img = models.ImageField(upload_to='img', verbose_name='图书图片')
    amount = models.IntegerField(default=1, verbose_name='库存量')
    has_sell = models.IntegerField(default=0, verbose_name='已售数量')
    price = models.FloatField(verbose_name='价格')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 创建时间 默认为当前时间
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book_category', verbose_name='分类')

    class Meta:
        verbose_name = "书籍管理"
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

class Order(models.Model):
    """
    订单表
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', verbose_name='用户')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='order_book', verbose_name='书籍')
    amount = models.IntegerField(default='1', verbose_name='数量')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')  # 申请时间

    class Meta:
        verbose_name = "订单管理"  # 设置模型的别名
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)


class Notice(models.Model):
    """
    公告
    """
    title = models.CharField(max_length=64, unique=True, verbose_name='公告标题')
    content = RichTextField(verbose_name='公告内容')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 创建时间 默认为当前时间

    class Meta:
        verbose_name = "公告管理"
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

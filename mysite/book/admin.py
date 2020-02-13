from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = '校园二手书管理系统'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    种类表的后台显示方式
    """
    list_display = ('name', 'create_at')  # 定义表头
    search_fields = ('name',)  # 定义检索项

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    书籍表的后台显示方式
    """
    list_display = ('name', 'description', 'amount', 'has_sell', 'price', 'create_at', 'category')  # 设置表头
    list_filter = ('category',)  # 定义过滤的方式
    search_fields = ('name',)  # 定义检索项

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    """
    定义公告的显示方式
    """
    list_display = ('title', 'create_at')


# def delete_selected(modeladmin, request, queryset):
#     """
#     删除订单
#     :param request:
#     :param queryset:
#     :return:
#     """
#     for obj in queryset:
#         obj.book.amount += obj.amount
#         obj.book.save()
#         obj.delete()
#     message = """成功删除订单"""
#     # self.message_user(request, message)
# delete_selected.short_description = '删除订单'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    定义订单的显示方式
    """
    list_display = ('user', 'get_book_name', 'amount', 'total_price', 'create_at')
    actions = ['delete_order']

    def get_book_name(self, obj):
        return obj.book.name
    get_book_name.short_description = '图书'

    def total_price(self, obj):
        return obj.amount * obj.book.price
    total_price.short_description = '总价'

    def get_actions(self, request):
        # 在actions中去掉‘删除’操作
        actions = super(OrderAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_order(self, request, queryset):
        """
        删除订单
        :param request:
        :param queryset:
        :return:
        """
        for obj in queryset:
            obj.book.amount += obj.amount
            obj.book.has_sell -= obj.amount
            obj.book.save()
            obj.delete()
        message = """成功删除所选订单"""
        self.message_user(request, message)
    delete_order.short_description = '删除所选的订单'

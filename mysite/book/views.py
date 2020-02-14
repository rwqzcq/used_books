import traceback

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

from .models import *
# Create your views here.

def index(request):
    """
    首页
    :param request:
    :return:
    """
    latest_books = Book.objects.all().order_by('-create_at')[0:4]
    latest_notices = Notice.objects.all().order_by('-create_at')[0:5]
    return render(request, 'book/index.html', {'latest_books' : latest_books, 'latest_notices' : latest_notices})


def book_list(request, cid):
    """
    分类下的所有图书
    :param request:
    :param cid:
    :return:
    """
    category = get_object_or_404(Category, id=cid)
    request.session['current_cid'] = cid
    books = category.book_category.all().order_by('-create_at')
    return render(request, 'book/list.html', {'books' : books})

def book_detail(request, bid):
    """
    图书详情
    :param request:
    :param bid:
    :return:
    """
    book = get_object_or_404(Book, id=bid)

    return render(request, 'book/detail.html', {'book' : book})

@require_POST
def search(request):
    """
    搜索图书
    :param request:
    :return:
    """
    # request.session.delete('current_cid')
    if 'current_cid' in request.session:
        del request.session['current_cid']
    name = request.POST['name']
    books = Book.objects.filter(name__contains=name)  # 模糊检索
    messages.success(request, name)
    # print(request.session['current_cid'])
    return render(request, 'book/list.html', {'books': books})

@require_POST
@login_required
def buy(request):
    """
    购买
    :param request:
    :return:
    """
    msg = ''
    error = 1
    order = Order()
    bid = request.POST['book_id']
    book = get_object_or_404(Book, id=bid)
    order.book = book
    user = request.user
    order.user = user
    already_have = book.amount - book.has_sell
    if already_have == 0:
        msg = '图书已经没有余量!'
    else:
        amount = int(request.POST['amount'])
        if amount > already_have:
            msg = '订购的数量超过了剩余量!'
        else:
            try:
                book.has_sell += amount
                book.save()
                order.amount = amount
                order.save()
                error = 0
                msg = '订购成功!'
            except:
                traceback.print_exec()
                msg = '保存失败!书籍信息没有更新成功!'

    return render(request, 'book/detail.html', {'book' : book, 'error' : error, 'message' : msg})


def notice_list(request):
    """
    公告详情
    :param request:
    :return:
    """
    notices = Notice.objects.all().order_by('-create_at')
    return render(request, 'notice/list.html', {'notices': notices})

def notice_detail(request, nid):
    """
    公告详情
    :param request:
    :param nid:
    :return:
    """
    notice = get_object_or_404(Notice, id=nid)
    return render(request, 'notice/detail.html', {'notice' : notice})


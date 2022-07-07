from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext
from bookTest.models import BookInfo,HeroInfo
# Create your views here.


def my_render(request,path,params):
    # 1.加载模板文件
    temp = loader.get_template(path)
    # 2. 获取上下文参数
    context = RequestContext(request, params)
    # 3，渲染模板文件：产生标准的html内容
    res_html = temp.render(context)
    return res_html


def index_view(request):
    # django 模板文件加载过程
    path = 'bookTest/index.html'
    params = {'context': "Hello Python", 'list': list(range(1, 10))}
    # 1.加载模板文件
    temp = loader.get_template('bookTest/index.html')
    # 2. 获取上下文参数
    context = RequestContext(request, {'context': "Hello Python", 'list': list(range(1, 10))})
    # 3，渲染模板文件：产生标准的html内容
    res_html = temp.render(context)
    # 4. 返回给浏览器
    my_html = my_render(request, path, params)
    render_html = render(request,path,params)
    return HttpResponse(render_html)


def show_books(request):
    books = BookInfo.objects.filter(isDelete=0)
    # books_notDelet = books.get(isDelete=0)
    books_html = render(request, "bookTest/show_books.html", {"books": books})
    return HttpResponse(books_html)


def detail(request, bid):
    hbook = BookInfo.objects.get(id=bid)
    print("bid:", bid)
    heroes = hbook.heroinfo_set.all()
    heroes_html = render(request,"bookTest/detail.html", {'heroes': heroes})
    return HttpResponse(heroes_html)


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.isDelete = True
    book.save()
    return HttpResponseRedirect("/books")


def create(request):

    create_html = render(request, "bookTest/create.html", {})

    return HttpResponse(create_html)


def create_book(request):
    if request.method == "POST":
        bname = request.POST.get("bname")
        bpub_date = request.POST.get("bpub_date")
        bread = request.POST.get("read")
        bcomment = request.POST.get("comment")
        b = BookInfo()
        b.btitle = bname
        b.bpub_date = bpub_date
        b.bread = bread
        b.bcomment = bcomment
        b.save()
        return HttpResponseRedirect("/books")


def index(request):
    return HttpResponse("Hello Python!")

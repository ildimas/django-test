from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.order_by("-id")
    # res = "<h1>Список новостей:</h1>"
    # for item in news:
    #     res += f"<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n"
        
    return render(request, 'news/VUZ_page.html', {'news': news, 'title': 'Список новостой'})

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
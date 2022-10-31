from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    news = News.objects.order_by("-id")
    # res = "<h1>Список новостей:</h1>"
    # for item in news:
    #     res += f"<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n"
        
    return render(request, 'news\main.html', {'news': news, 'title': 'Список новостой'})

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news\category.html', {'news': news, 'category': category})
def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news\\view_news.html', {'news_item': news_item})
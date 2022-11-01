from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category
import folium
from dadata import Dadata

token = 'C2313134123'
secret = 'QWERTFDBDF2134'

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
def misha(request):
    #Делаем карту
    m = folium.Map(location=[55.9, 37.7])
    
    folium.Marker([5.594, -0.219]).add_to(m)
    
    m = m._repr_html_()
    context = {'m': m,}
    return render(request, 'news\index.html', context=context)
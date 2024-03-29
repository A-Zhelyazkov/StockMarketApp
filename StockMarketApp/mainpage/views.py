from django.shortcuts import render


def index_view(request):
    return render(request, 'mainpage/index.html')


def news_view(request):
    return render(request, 'mainpage/news_page.html')

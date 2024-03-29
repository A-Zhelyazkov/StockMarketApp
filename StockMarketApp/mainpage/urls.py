from django.urls import path

from StockMarketApp.mainpage.views import index_view, news_view

urlpatterns = [
    path('', index_view, name='home_page'),
    path('news/', news_view, name='news_page'),
]
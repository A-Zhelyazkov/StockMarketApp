from django.urls import path

from StockMarketApp.stocks.views import market_view

urlpatterns = [
    path('market/', market_view, name='view_market'),
]
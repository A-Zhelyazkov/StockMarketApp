from django.urls import path

from StockMarketApp.portfolio.views import portfolio_view

urlpatterns = [
    path('', portfolio_view, name='portfolio_view'),
]
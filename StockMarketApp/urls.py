
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('StockMarketApp.mainpage.urls')),
    path('stocks/', include('StockMarketApp.stocks.urls')),
    path('portfolio/', include('StockMarketApp.portfolio.urls')),
    path('users/', include('StockMarketApp.users.urls')),
]

from django.urls import path

from StockMarketApp.users.views import login_user_view, register_user_view

urlpatterns = [
    path('login/', login_user_view, name='login_user'),
    path('register/', register_user_view, name='register_user'),
]
from django.urls import path

from StockMarketApp.users.views import index_view, login_user_view, register_user_view

urlpatterns = [
    path('', index_view),
    path('login/', login_user_view, name='login_user'),
    path('register/', register_user_view, name='register_user'),
]
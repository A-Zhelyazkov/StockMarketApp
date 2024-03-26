from django.shortcuts import render

def index_view(request):
    return render(request, 'mainpage/index.html')


def login_user_view(request):
    return render(request, 'user/login_page.html')


def register_user_view(request):
    return render(request, 'user/register_page.html')
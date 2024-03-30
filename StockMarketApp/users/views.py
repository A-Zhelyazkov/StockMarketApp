from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from StockMarketApp.users.models import Profile


def login_user_view(request):
    return render(request, 'user/login_page.html')


def register_user_view(request):
    return render(request, 'user/register_page.html')


class DetailsProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "user/profile_details_page.html"


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "user/edit_details_page.html"
    fields = ('profile_picture', 'first_name', 'last_name', 'date_of_birth')
    success_url = reverse_lazy('home_page')


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'user/delete_profile_page.html'
    success_url = reverse_lazy('home_page')
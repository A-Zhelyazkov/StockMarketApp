from django.urls import path, include

from StockMarketApp.users.views import login_user_view, register_user_view, DetailsProfileView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('login/', login_user_view, name='login_user'),
    path('register/', register_user_view, name='register_user'),
    path("<int:pk>/", include([
        path("", DetailsProfileView.as_view(), name="profile_details"),
        path("edit/", EditProfileView.as_view(), name="edit_profile_details"),
        path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
    ])),
]
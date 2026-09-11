from django.urls import path
from .views import (MyLogoutPage,UserListView,AboutMeView)
from django.contrib.auth.views import LoginView,LogoutView


app_name = "myauth"

urlpatterns = [
    # path("login/",login_view,name='login'),
    path(
        "login/",
        LoginView.as_view(
            template_name='myauth/login.html',
            redirect_authenticated_user=True
            ),
            name='login'),
    #path('logout/',logout_view,name='logout'),  
    path('logout/',MyLogoutPage.as_view(),name='logout'), 
    path('list_users/',UserListView.as_view(),name='list_users'),
    path("about_me/", AboutMeView.as_view(), name="about_me_url"),
    ]

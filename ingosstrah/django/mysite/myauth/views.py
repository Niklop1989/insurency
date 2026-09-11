from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views import View
from django.contrib.auth.models import User

from django.contrib.auth.views import LogoutView
from django.views import View
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DetailView


class MyLogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('myauth:login')

class UserListView(ListView):
    template_name = "myauth/list_users.html"
    context_object_name = 'list_users'
    queryset = User.objects.all()    

class AboutMeView(TemplateView):
    template_name = 'myauth/about_me.html'    
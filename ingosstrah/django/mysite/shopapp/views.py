from django.shortcuts import render

from django.shortcuts import (render,redirect,reverse,get_object_or_404,)
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from timeit import default_timer
from django.contrib.auth.models import Group,User
from django.views import View
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)

import uuid
from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Insurance, UserPolicy

class InsuranceListView(ListView):
    """Главная страница: каталог страховок с фильтрацией"""
    model = Insurance
    template_name = 'insurance_list.html'
    context_object_name = 'insurances'

    #def get_queryset(self):
    #    queryset = Insurance.objects.filter(is_active=True)
    #    category = self.request.GET.get('category')
    #    if category:
    #        queryset = queryset.filter(category=category)
    #    return queryset


class ProfilePoliciesListView(LoginRequiredMixin, ListView):
    """Личный кабинет: список полисов пользователя и проверка дедлайнов"""
    model = UserPolicy
    template_name = 'profile_policies.html'
    context_object_name = 'policies'
    login_url = reverse_lazy('login') 

    def get_queryset(self):
        queryset = UserPolicy.objects.filter(user=self.request.user).order_by('end_date')
        current_date = timezone.now().date()
        
        # Автоматическое обновление просроченных статусов в БД
        for policy in queryset:
            if policy.end_date < current_date and policy.status == 'active':
                policy.status = 'expired'
                policy.save(update_fields=['status'])
                
        return queryset


class BuyInsuranceView(LoginRequiredMixin, RedirectView):
    """Процесс оформления полиса в БД и редирект в личный кабинет"""
    permanent = False
    query_string = True
    pattern_name = 'profile_policies'

    def get_redirect_url(self, *args, **kwargs):
        insurance_id = kwargs.get('insurance_id')
        insurance = get_object_or_404(Insurance, id=insurance_id)
        
        start = timezone.now().date()
        end = start + timedelta(days=365)
        
        new_policy = UserPolicy.objects.create(
            user=self.request.user,
            insurance=insurance,
            policy_number=f"POL-{uuid.uuid4().hex[:8].upper()}",
            start_date=start,
            end_date=end,
            status='active'
        )
        
        messages.success(
            self.request, 
            f"Полис {new_policy.policy_number} успешно оформлен! Срок действия до {end.strftime('%d.%m.%Y')}."
        )
        return super().get_redirect_url(*args, **kwargs)

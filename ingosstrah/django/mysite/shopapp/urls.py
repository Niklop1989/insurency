from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
app_name = "shopapp"

from . import views

urlpatterns = [
    path('', views.InsuranceListView.as_view(), name='insurance_list'),
    path('my-policies/', views.ProfilePoliciesListView.as_view(), name='profile_policies'),
    path('buy/<int:insurance_id>/', views.BuyInsuranceView.as_view(), name='buy_insurance'),
    
]


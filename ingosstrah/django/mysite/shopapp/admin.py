from io import TextIOWrapper
from csv import DictReader


from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
#from .admin_mixins import ExportAsCSVMixin
#from .forms import CSVImportForm


from django.contrib import admin
from .models import Insurance

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке всех записей
    list_display = ('id', 'price', 'is_active')
    
    # Поля, по которым можно кликнуть для перехода к редактированию
    list_display_links = ('id', 'price')
    
    # Фильтры в правой колонке (удобно для логических полей)
    list_filter = ('is_active',)
    
    # Возможность быстро переключать активность прямо из списка
    list_editable = ('is_active',)
    
    # Поля для поиска (добавьте сюда другие текстовые поля, если они есть, например 'name')
    search_fields = ('id',)

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext_lazy,ngettext

from django.utils import timezone
from datetime import timedelta


class Insurance(models.Model):
    # Категории страхования для удобной фильтрации и работы с БД
    CATEGORY_CHOICES = [
        ('auto', 'Автострахование'),
        ('health', 'Медицина'),
        ('property', 'Имущество'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название страховки")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание условий")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена в год (руб.)")
    is_active = models.BooleanField(default=True, verbose_name="Доступно для покупки")

    class Meta:
        verbose_name = "Страховой продукт"
        verbose_name_plural = "Страховые продукты"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


def auto_prewiew_directory_path(instance:"UserPolicy",filename:str)->str:
    return 'users_polices/auto_{pk}/prewiew/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )

class UserPolicy(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активен'),
        ('expired', 'Истёк'),
        ('canceled', 'Аннулирован'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='policies', verbose_name="Клиент")
    insurance = models.ForeignKey('Insurance', on_delete=models.PROTECT, verbose_name="Страховой продукт")
    policy_number = models.CharField(max_length=50, unique=True, verbose_name="Номер полиса")
    
    start_date = models.DateField(default=timezone.now, verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Статус")
    user_auto = models.TextField(null=True,blank=True)
    prewiew = models.ImageField(null=True,blank=True,upload_to=auto_prewiew_directory_path)
    

    class Meta:
        verbose_name = "Купленный полис"
        verbose_name_plural = "Купленные полисы"

    # Автоматически проверяем, не истек ли полис
    @property
    def is_expired(self):
        return timezone.now().date() > self.end_date

    # Считаем, сколько дней осталось до конца страховки
    @property
    def days_left(self):
        if self.is_expired:
            return 0
        delta = self.end_date - timezone.now().date()
        return delta.days

    def __str__(self):
        return f"Полис №{self.policy_number} ({self.user.username})"

    

def auto_images_directory_path(instance:'AutoImage',filename:str)->str:
     return 'autos/auto_{pk}/images/{filename}'.format(
        pk=instance.auto.pk,
        filename=filename,
    )
class AutoImage(models.Model):
    auto = models.ForeignKey(UserPolicy,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to=auto_images_directory_path)
    description = models.TextField(max_length=200,null=False,blank=True)


from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name="الشركة المصنعة")
    model_name = models.CharField(max_length=50, verbose_name="الموديل")
    description = models.TextField(verbose_name="الوصف")
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر اليومي")
    image = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name="صورة السيارة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Device(models.Model):
    status_devices = [
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    type_devices = [
        ('low','low'),
        ('middle','middle'),
        ('high','high'),
    ]
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    photo_device = models.ImageField(upload_to='photos', null=True, blank=True, help_text="يجب ان تكون بصيغة jpg or webp or jpeg")
    photo_company = models.ImageField(upload_to='photos', null=True, blank=True, help_text="يجب ان تكون بصيغة jpg or jpeg or webp")
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_money = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    type_device = models.CharField(max_length=50, choices=type_devices, null=True, blank=True)
    rental_price_hour =  models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_period = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_rental = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_devices, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
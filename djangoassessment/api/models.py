from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group
from django.utils.translation import gettext as _
from django.conf import settings


# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)
    date = models.DateField()
    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="userpost",blank=True,null=True)
    
    def  __str__(self) -> str:
        return f"Invoice {self.invoice_number} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for Invoice {self.invoice.invoice_number}: {self.description}"

class CustomUsers(AbstractUser):
    class Meta:
        permissions = [
            ("can_manage_custom_groups", "Can manage custom groups"),
        ]  
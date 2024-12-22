from django.db import models

# Create your models here.
class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for {self.lease.property.title} by {self.lease.tenant.username} - {self.amount}"


class Customer(AbstractUser):
    is_landlord = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.address}"



    

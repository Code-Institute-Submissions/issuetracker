from django.db import models

# Create your models here.
class Package(models.Model):
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    features1=models.TextField()
    features2=models.TextField()
    features3=models.TextField()
    features4=models.TextField()
    
    def __str__(self):
        return self.description
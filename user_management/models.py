from django.db import models

# Create your models here.
class UserInfo(models.Model):
    full_name = models.CharField(max_length=50, blank=False, null=False)
    address_1 = models.CharField(max_length=100, blank=False, null=False)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zip_num = models.CharField(max_length=9, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)

    def str(self):
        return self.username
    

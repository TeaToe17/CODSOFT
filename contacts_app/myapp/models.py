from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"
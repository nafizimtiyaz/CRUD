from django.db import models

class book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200,blank=False)
    a_name=models.CharField(max_length=200,blank=False)
    price=models.CharField(max_length=200,blank=False)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Book'


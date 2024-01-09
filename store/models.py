from django.db import models

# Create your models here.
class product(models.Model):
    product_id  = models.AutoField
    product_name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    images = models.ImageField(upload_to="store/images" ,default="")

    def __str__(self):
        return self.product_name

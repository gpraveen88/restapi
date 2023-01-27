from django.db import models

# Create your models here.




class productMainModel(models.Model):
    
    size_choice=(
        ('10','10'),
        ('20','20'),
        ('30','30'),
    )
    quality_choice=(
        ('high','high'),
        ('low','low'),
        ('medium','medium'),
    )
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Price=models.IntegerField()
    unique_code=models.IntegerField(unique = True)
    Size = models.CharField(choices=size_choice,max_length=10)
    Quality = models.CharField(choices=quality_choice,max_length=10)

    def __str__(self):
        return str(self.Title)


class productColourModel(models.Model):
    colour_choice=(
        ('red','red'),
        ('blue','blue'),
        ('green','green'),
        ('black','black'),
    )
    Product = models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Colour = models.CharField(choices=colour_choice,max_length=100)

    def __str__(self):
        return str(self.Product)

class productImageModel(models.Model):
    Product = models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Image   = models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=100)
    
    def __str__(self):
        return str(f"{self.Product} image of the product")


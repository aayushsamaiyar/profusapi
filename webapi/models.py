from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
  
class categories(models.Model):
   cate_id = models.CharField(max_length=10,primary_key=True)
   cate_name  = models.CharField(max_length=50, default="name")
   cate_desc = models.CharField(max_length=100)

   def __str__(self):   
      return self.cate_name

class items(models.Model):
   item_id = models.CharField(primary_key=True, max_length=10)
   cate_id = models.ForeignKey(categories, null =True, on_delete=models.CASCADE)
   item_name = models.CharField(max_length=100, default="item name")
   item_info = models.CharField(max_length=100,default="any information of type")
   item_price = models.IntegerField(default=0)

   def __str__(self):
      return self.item_name
      

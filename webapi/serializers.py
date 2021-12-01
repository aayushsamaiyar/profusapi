from rest_framework import serializers
from .models import categories, items

class categoriesSerializer (serializers.ModelSerializer):
   class Meta:
      model = categories
      fields = ('cate_id','cate_name')
      # fields = "__all__"

class itemSerializer(serializers.ModelSerializer):
   class Meta:
      model = items
      fields = ('item_id','item_name')
      # fields ="__all__"

class itemViewSerializer(serializers.ModelSerializer):
   class Meta:
      model = items
      fields = ('item_name','item_info','item_price')
      # fields ="__all__"
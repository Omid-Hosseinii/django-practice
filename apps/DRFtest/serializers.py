from rest_framework import serializers
from .models import *

### first 5 video
class PersonSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    family=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    email=serializers.EmailField(max_length=30)
    
    
    
class PersonSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'    
    
class ProductSerializer3(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'    
    
    
    
    
def checkFamily(value):
    if value[0]!='r':
        raise serializers.ValidationError("نام خانوادگی باید با حرف ار شروع شود")    
    
    
class PersonSerializer3(serializers.ModelSerializer):
    re_name=serializers.CharField(max_length=30,write_only=True)
    class Meta:
        model=Person
        fields='__all__'    
        #exclude=['name']
        extra_kwargs={
            'name':{'write_only':True},
            'family':{'validators':(checkFamily,)}
        }
        
        
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("نام باید بیشتر از 4 کارکتر باشد")
        return value   
    
    def validate(self,data):
        if data['name']!=data['re_name']: 
            raise serializers.ValidationError("نام و تکرار آن مشابه نیست")
        if len(data['family']) < 4:
            raise serializers.ValidationError("نام خانوادگی باید بیشتر از 4 کارکتر باشد")
        return data    
        
    def create(self,validated_data):
        del validated_data['re_name']
        return Person.objects.create(**validated_data) 
    
#_______________________________________________________________________    
### second 5 video       


class ProductSerializer(serializers.ModelSerializer):
    features=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'
        extra_kwargs={
            "name":{'write_only':True}
        }
      
    def get_features(self,obj):
        res=obj.features.all()
        return ProductFeatureSerializer(instance=res,many=True).data    
        
class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductFeature
        fields='__all__'  
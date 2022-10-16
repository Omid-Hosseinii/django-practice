from multiprocessing import context
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from CustomPermission import CustomPermissionForProductFeature
# Create your views here.


def index(request):
    return render(request,'DRFtest/index.html')

@api_view(['GET', 'POST'])
def api_1(request):
    context={
        'name':'omid',
        'family':'hosseini',
        'age':26
    }
    return Response(context)

class api2(APIView):
    def get(self,request):
        context={    
            'name':'omid',
            'family':'hosseini',
            'age':26
        }
        return Response(context)
        
class api3(APIView):
    def get(self,request,name,family,age):
        context={    
            'name':name,
            'family':family,
            'age':age
        }
        return Response(context)



class api4(APIView):
    def get(self,request):
        ### how to read querystring 
        name=request.GET['name']
        family=request.GET.get('family')
        age=request.query_params['age']

        context={    
            'name':name,
            'family':family,
            'age':age
        }
        return Response(context)
    
    
class PersonList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        people=Person.objects.all() 
        ser_data=PersonSerializer(instance=people,many=True)
        
        return Response(data=ser_data.data)          


    
class PersonSearch(APIView):
    def get(self,request,code):
        try:
            
            person=Person.objects.get(id=code) 
            ser_data=PersonSerializer(instance=person)
            return Response(data=ser_data.data)   
        except:
            return Response('Not Found... !')   
                   

#### solution one for add in api
class PersonAdd(APIView):
    def post(self,request):
        ser_data=PersonSerializer(data=request.POST) 
        if ser_data.is_valid():
            Person.objects.create(
                name=ser_data.validated_data['name'],
                family=ser_data.validated_data['family'],
                age=ser_data.validated_data['age'],
                email=ser_data.validated_data['email']
            )
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)    
        # return Response("error")
        return Response(ser_data.errors)
    
    
    
    
class PersonList2(APIView):
    def get(self,request):
        people=Person.objects.all() 
        ser_data=PersonSerializer2(instance=people,many=True)
        return Response(data=ser_data.data)      
    
#### solution two for add in api (if we have file or image we use request.data)   
class ProductAdd(APIView):
    def post(self,request):
        ser_data=ProductSerializer3(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)      
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)      
    
#### solution three for add in api    
class PersonAdd2(APIView):
    def post(self,request):
        ser_data=PersonSerializer3(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)    
        # return Response("error")
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
#------------------------------------------------------------------------------------------------


### this class can create token for all user by run url's
class CreateTokenUser(APIView):
    
    def get(self,request):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK)
    
    
class ProductShow(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        products=Product.objects.all() 
        ser_data=ProductSerializer(instance=products,many=True)
        
        return Response(data=ser_data.data)     
    
    
    
    
class DeleteProductFeature(APIView):
    permission_classes=[CustomPermissionForProductFeature] 
    
    def delete(self,request,pk):
        try:
            product_feature=ProductFeature.objects.get(pk=pk)            
            self.check_object_permissions(request,product_feature)   ### call has_permission function
            product_feature.delete()
            return Response('ویژگی مورد نظر با موفقیت حذف شد')
        except ProductFeature.DoesNotExist:
            return Response('ویژگی مورد نظر یافت نشد')   
           
from django.urls import path
from .views import *
### for recived token by user when give user username and password
from rest_framework.authtoken import views as auth_views
### for jwt token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('',index,name='drfmain'),
    path('apitest1',api_1,name='apitest1'),
    path('apitest2',api2.as_view(),name='apitest2'),
    path('apitest3/<str:name>/<str:family>/<int:age>',api3.as_view(),name='apitest3'),
    path('apitest4',api4.as_view(),name='apitest4'),
    path('apitest5',PersonList.as_view(),name='apitest5'),
    path('apitest6/<int:code>',PersonSearch.as_view(),name='apitest6'),
    path('apitestadd/',PersonAdd.as_view(),name='apitestadd'),
    path('apitest8',PersonList2.as_view(),name='apitest8'),
    path('apitest9',ProductAdd.as_view(),name='apitest9'),
    path('apitest10',PersonAdd2.as_view(),name='apitest10'),
    #----------------------------------------------------------------
    
    ### for recived token by user when give user username and password
    path('apitokenbyuser',auth_views.obtain_auth_token,name='apitokenbyuser'),
    ### create token for all user
    path('createtokenalluser/',CreateTokenUser.as_view(),name='createtokenalluser'),
    path('productshow/',ProductShow.as_view(),name='productshow'),
    path('deletefeature/<int:pk>/',DeleteProductFeature.as_view(),name='deletefeature'),
    ### for jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]




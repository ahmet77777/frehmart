"""
URL configuration for freshmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from .views import *
from rest_framework_simplejwt.views import TokenVerifyView,TokenObtainPairView,TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('error_404',error_404),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/drf_auth/',include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('adminpanel/',include('adminpanel.urls')),
    path('',include('shop.urls')),
    
    # Category API

    path('api/v1/category/',CategoryAPIList.as_view()),
    path('api/v1/category/<int:pk>',CategoryAPIUpdate.as_view()),
    path('api/v1/categorydelete/<int:pk>',CategoryAPIDestroy.as_view()),

    # Subcategory API
    
    path('api/v1/subcategory/',SubcategoryAPIList.as_view()),
    path('api/v1/subcategory/<int:pk>',SubcategoryAPIUpdate.as_view()),
    path('api/v1/subcategorydelete/<int:pk>',SubcategoryAPIDestroy.as_view()),

    # Product API

    path('api/v1/product/',ProductAPIList.as_view()),
    path('api/v1/product/<int:pk>',ProductAPIUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>',ProductAPIDestroy.as_view()),

    # Order API

    path('api/v1/order/',OrderAPIList.as_view()),
    path('api/v1/orderdelete/<int:pk>',OrderAPIDestroy.as_view())
    
 
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

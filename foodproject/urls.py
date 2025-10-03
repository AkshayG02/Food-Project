"""
URL configuration for foodproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home_page.as_view(),name='home'),
    path('c/', views.AddFood.as_view()),
    path('list/', views.FoodList.as_view(),name = "food_list"),
    path('detail/<int:pk>', views.FoodDetails.as_view(),name='detail'),
    path('update/<int:pk>', views.FoodUpdate.as_view()),
    path('delete/<int:pk>', views.FoodDelete.as_view()),
    
    
    
    path("", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.CustomSignupView.as_view(), name="signup"),
    # path("home/", views.HomeView.as_view(), name="home"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),


    #add to cart
    path("cart/", views.CartView.as_view(), name='cart'),
    path("add_to_cart/<int:food_id>/", views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),


    #add contact
    path("contact/", views.ContactView.as_view(), name='contact'),



]

# To upload images inside data base model 
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

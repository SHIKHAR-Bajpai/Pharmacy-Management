#from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path("" , views.index , name="ShopHome"),
    path("about/", views.about, name="about"),
    path("login/", views.login_call, name="login"),
    
    path("userlogin/", views.login_call, name="userlogin"),
    path("signup/" , views.signup, name="signup"),
    path("logout/" , views.logout_call , name='logout'),

    
    path("heart/" , views.heart, name="heart"),
    path("diabetes/" , views.diabetes, name="diabetes"),
    path("liver/" , views.liver, name="liver"),
    path("skin/" , views.skin, name="skin"),
    # path("search/", views.search, name="search"),
    # path("productview/", views.product, name="product"),
    # path("checkout/", views.checkout, name="checkout"),
    
]

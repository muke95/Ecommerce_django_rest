from django.urls import path
from ecomapp import views 


urlpatterns =[
    path("",views.response,name="response"),
    path("product/",views.get_product,name="getProduct"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart_view, name='cart'),
]
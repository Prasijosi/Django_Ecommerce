from django.urls import path,include
from products import views

urlpatterns = [
    path('list',views.listproducts,name="list"),
]

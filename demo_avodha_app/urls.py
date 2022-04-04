from django.contrib import admin
from django.urls import path
from demo_avodha_app import views

app_name='myapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('shop/<int:shop_id>',views.detail,name='detail'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete')

]

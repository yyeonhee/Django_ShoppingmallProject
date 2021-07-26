from django.urls import path
from . import views 


urlpatterns = [
    path('create', views.create, name="create"),
    path('detail/<str:id>', views.detail, name="detail"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('order/<str:id>', views.order, name="order"),
    path('order_list', views.order_list, name="order_list"),
    path('order_finished', views.order_finished, name="order_finished"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name='home'),
    path('father', views.father),
    path('detail/<int:todo_id>/', views.detail, name='details'),
    path('delete/<int:todo_id>/',views.delete, name='delete')
]

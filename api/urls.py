from django.urls import path
from . import views
urlpatterns = [
    path('list',views.listAPI.as_view()),
     path('delete/<int:pk>',views.DeleteAPI.as_view()),
    
]

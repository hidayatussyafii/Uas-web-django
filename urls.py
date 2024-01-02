from django.urls import path
from . import views
from . import templates




urlpatterns = [
    path('members/', views.members, name='members'),
    

]
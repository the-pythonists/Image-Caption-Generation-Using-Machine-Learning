from django.urls import path
from HomeApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('caption/',views.caption,name='caption'),
]

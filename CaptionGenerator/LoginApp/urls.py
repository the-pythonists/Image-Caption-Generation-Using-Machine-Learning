from django.urls import path
# from django.contrib.auth import views as auth_views
from LoginApp import views
from LoginApp.models import Register
from django.views.generic.detail import DetailView

urlpatterns = [
    # path('',views.index,name='index'),
    path('', views.RegisterView.as_view(), name='register_view'),
    path('logout/',views.logout,name='logout'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('home/',views.HomeClass.as_view(),name='home'),
    path('sessioncheck/',views.SessionCheckView.as_view(),name='sesion'),
]

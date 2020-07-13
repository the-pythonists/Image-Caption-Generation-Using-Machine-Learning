from django.urls import path
# from django.contrib.auth import views as auth_views
from LoginApp import views
 

urlpatterns = [
    # path('',views.index,name='index'),
    path('', views.LoginView.as_view(), name='login_view'),
    path('test',views.test,name='test'),

]

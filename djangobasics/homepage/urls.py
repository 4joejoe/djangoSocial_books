from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('upload',views.upload_file,name='create_post')
]
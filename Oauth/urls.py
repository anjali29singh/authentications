from django.urls import path, include

from . import views
urlpatterns = [
    path('login/',views.github_login,name='github_login'),
    path('logout/',views.logout,name='logout'),
    path('callback/',views.github_callback,name='github_callback')
    
]

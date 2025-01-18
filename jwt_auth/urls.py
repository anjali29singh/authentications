from django.urls import include, path

from .views import signup , signin
urlpatterns = [

    path('signup/',signup,name='signup'), # signup with email or username
    path('signin/',signin,name='signin'), # signin with email or username
    # path('signup_google/', view=views.signup_google,name='signup_google'), # signup with google
    # path('signin_google/', view=views.signin_google,name='signin' ), # signup with google
    # path('homepage/',view=views.homepage,name='homepage'), # homepage after login

    # path('logout/',view=views.logout,name='logout'), # logout

    # path('callback/',view= views.callback,name='callback'), # callback after login
]


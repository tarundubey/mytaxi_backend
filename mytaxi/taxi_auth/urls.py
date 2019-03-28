#from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views.views import token, revoke_token

urlpatterns = [
    path('login/', token),
    path('logout/',revoke_token)
    #     path('users/', UserView.as_view()),
 ]

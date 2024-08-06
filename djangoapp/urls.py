from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), #way to connect react app
    path('api/btn-data/', views.btnData, name='btndata'), # way to get data from the react to django
    path('api/get-csrf-token/', views.get_csrf_token, name='get_csrf_token') # way to provide csrf token to react
]

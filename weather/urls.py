from django.urls import path
from .views import *
from .api_views import *

urlpatterns = [
    path('',index, name="home_page" ),
    path('api/city/', getAllCities, name="all_cities" ),
    path('api/city/add', addCity, name="add_cities" ),
    path('api/city/<int:id>', getCity, name="get_city" ),
    path('api/city/update/<int:id>', CityUpdate, name="city_update" ),
    path('api/city/delete/<int:id>', cityDelete, name="city_delete" ),

]

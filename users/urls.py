from django.urls import include
from django.urls import path
from knox import views as knox_views
from rest_framework import routers
from rest_framework.authtoken import views

from users.views import UserViewSet, RegisterAPI, LoginAPI, CountryViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

from dj_rest_auth.views import LoginView
from django.urls import path, include


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]

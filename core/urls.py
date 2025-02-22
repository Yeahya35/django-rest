from django.urls import path
from .token import *
from .views import *


urlpatterns = [
    path("login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("set-csrf-cookie", set_csrf_token, name="logout"),
    path("refresh", RefreshViewSet.as_view(), name="token_refresh"),
    path("register", register, name="register"),
]
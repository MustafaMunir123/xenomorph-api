from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from xenomorph_api.apps.users.api.v1.views import UserApiView
from django.urls import path

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/register/", UserApiView.as_view()),
]


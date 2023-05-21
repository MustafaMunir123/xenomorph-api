from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from xenomorph_api.apps.users.api.v1.views import (
    UserApiView,
    UserLogin
)
from django.urls import path

urlpatterns = [
    path("api/token/", UserLogin.as_view(), name='token_obtain_pair'),
    path("api/register/", UserApiView.as_view()),
    path("api/all/", UserApiView.as_view()),
]


from django.urls import path
from xenomorph_api.apps.tracking.api.v1.views import TrackingAPIView

urlpatterns = [
    path("api/v1/tracks/", TrackingAPIView.as_view()),
]

from django.urls import path
from xenomorph_api.apps.tracking.api.v1.views import (
    TrackingAPIView,
    FeedbackAPIView
)

urlpatterns = [
    path("api/v1/tracks/", TrackingAPIView.as_view()),
    path("api/v1/feedback/", FeedbackAPIView.as_view())
]

import uuid
from rest_framework.views import APIView
from rest_framework.views import status
from xenomorph_api.apps.tracking.api.services import TrackingService
from xenomorph_api.apps.email_service import send_email
from xenomorph_api.apps.tracking.models import (
    Tracks,
    Mark
)
from xenomorph_api.apps.services import success_response
from xenomorph_api.apps.tracking.api.v1.serializers import (
    TrackingSerializer,
    UserFeedbackSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TrackingAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get_weather_news_hotels(cities):
        try:
            data_list = []
            for city in cities:
                # Weather
                data_dict = {"weather": TrackingService.get_aggregated_weather(city)}

                # City Hotels
                if TrackingService.get_aggregated_hotels(city):
                    data_dict = {"hotels": TrackingService.get_aggregated_hotels(city)}

                # News
                data_dict["News"] = TrackingService.get_aggregated_news(city)
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            raise ValueError(f"Unable to fetch data")

    @staticmethod
    def create_many_marks(track_id, marks_list):
        track = Tracks.objects.get(id=track_id)
        for mark in marks_list:
            mark_obj = Mark.objects.create(track=track, location=mark)
            mark_obj.save()

    @staticmethod
    def get_serializer():
        return TrackingSerializer

    def post(self, request):
        try:
            print("sdsh")
            print(request.data)
            marks = request.data.pop("marks")
            request.data["id"] = uuid.uuid4()
            serializer = self.get_serializer()
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            city_list = [serializer.validated_data['origin_location'], *marks,
                         serializer.validated_data['destination_location']]
            cities_data = self.get_weather_news_hotels(city_list)
            self.create_many_marks(serializer.validated_data["id"], marks)

            return success_response(status=status.HTTP_200_OK, data=cities_data)
        except Exception as ex:
            raise ex

    def get(self, request):
        try:
            tracks = Tracks.objects.all()
            serializer = self.get_serializer()
            serializer = serializer(tracks, many=Tracks)
            return success_response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            raise ex


class FeedbackAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_serializer():
        return UserFeedbackSerializer

    def post(self, request):
        try:
            request.data["user_id"] = request.user.user_id
            serializer = self.get_serializer()
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            send_email(to="mustafamunir10@gmail.com", subject="User Feedback",
                       body=serializer.validated_data["feedback"])
            return success_response(status=status.HTTP_200_OK, data=serializer.validated_data)
        except Exception as ex:
            raise ex

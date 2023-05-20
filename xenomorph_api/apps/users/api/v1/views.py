# from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.views import status
from xenomorph_api.apps.services import success_response
from xenomorph_api.apps.users.models import User
from xenomorph_api.apps.users.api.v1.serializers import UserSerializer

# Create your views here.


class UserApiView(APIView):

    @staticmethod
    def get_serializer():
        return UserSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer()
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            raise ex

    def get(self, request):
        try:
            users = User.objects.all()
            serializer = self.get_serializer()
            serializer = serializer(users, many=True)
            return success_response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            raise ex

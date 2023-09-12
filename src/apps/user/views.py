from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from src.apps.user.models import User
from src.apps.user.serializers import UserRegisterSerializer, UserSerializer


class RegisterView(APIView):
    # permission_classes = (IsAdminUser,)
    serializer_class = UserRegisterSerializer

    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenObtainPairView):
    pass


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get()
        if response.status_code == 200:
            user = self.user
            role = user.role
            response.data['role'] = role
        return response


class Profile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request) -> Response:
        user = User.objects.get(name=request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLisView(APIView):

    def get(self, request) -> Response:
        user = User.objects.all().only('name', 'surname', 'phone')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoleListView(APIView):

    def get(self, request) -> Response:
        queryset = User.STATUS_CHOICES
        status_list = [{role[0]: role[1]} for role in queryset]
        return Response(status_list, status=status.HTTP_200_OK)

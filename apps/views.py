from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Student
from apps.serializers import StudentRegisterModelSerializer, StudentUpdateModelSerializer, StudentLoginSerializer
from send_email import send_email


class StudentCreateApiView(CreateAPIView):
    serializer_class = StudentRegisterModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        subject = 'Ro\'yxatdan o\'tdingiz'
        message = 'Siz ro\'yxatdan o\'tdingiz'
        recipients = [email]
        success, result = send_email(subject, message, recipients)
        if success:
            return Response({'message': 'Siz ro\'yxatdan o\'tdingiz va email yuborildi'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Emailni yuborishda xatolik yuz berdi'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentLoginAPIView(APIView):
    serializer_class = StudentLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Noto\'g\'ri email yoki parol'}, status=status.HTTP_400_BAD_REQUEST)


class StudentUpdateApiView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentUpdateModelSerializer
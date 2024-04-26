from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

from apps.models import Student
from rest_framework.serializers import ModelSerializer, EmailField, CharField


class StudentRegisterModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('image', 'first_name', 'last_name', 'email', 'phone_number',)


class StudentLoginSerializer(ModelSerializer):
    email = EmailField()
    password = CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise ValidationError("Foydalanuvchi bloklangan hisob kitobidir.")
            else:
                raise ValidationError("Noto'g'ri email yoki parol kiritdingiz.")
        else:
            raise ValidationError("Email va parol kiritishingiz kerak.")
        return data


class StudentUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('image', 'first_name', 'last_name', 'email', 'phone_number',)
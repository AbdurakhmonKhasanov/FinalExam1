from django.urls import path
from apps.views import StudentUpdateApiView, StudentCreateApiView, StudentLoginAPIView

urlpatterns = [
    path('student-register/', StudentCreateApiView.as_view(), name='register_student'),
    path('student-login/', StudentLoginAPIView.as_view(), name='login_student'),
    path('student-update/<int:pk>', StudentUpdateApiView.as_view(), name='update_student'),
]
from django.urls import path
from .views import RegisterView, GenericAPIView, apiOverview
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', apiOverview, name='apiOverview'),
    path('register/', RegisterView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('generic/<int:id>/', GenericAPIView.as_view()),
]

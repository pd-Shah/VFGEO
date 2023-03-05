from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    MunicipalityList,
    MunicipalityDetail,
)

router = DefaultRouter()

urlpatterns = [
    path("municipality/", MunicipalityList.as_view()),
    path("municipality/<int:pk>/", MunicipalityDetail.as_view()),
]

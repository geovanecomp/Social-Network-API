from django.urls import path, include

from rest_framework.routers import DefaultRouter

from posterr_api import views


router = DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]

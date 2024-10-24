from django.urls import path
from threef.views import ThreadViewSet, CommentViewSet, RegisterationAPIView, LoginAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'thread', ThreadViewSet)
router.register(r'comment', CommentViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('register/', RegisterationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]

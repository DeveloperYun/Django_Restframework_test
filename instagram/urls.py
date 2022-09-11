from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개 URL을 생성
# 생성된 2개의 URL이 router.urls 에 리스트 형태로 존재하게됨.


urlpatterns = [
    path('mypost/<int:pk>/',views.PostDetailAPIView.as_view()),
   # path('public/', views.public_post_list),
    path('', include(router.urls)),
]

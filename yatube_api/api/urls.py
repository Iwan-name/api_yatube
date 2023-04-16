from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<posts_id>\d+/comments)',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]

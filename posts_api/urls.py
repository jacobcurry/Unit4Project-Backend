from django.urls import path
from . import views

urlpatterns = [
    path('api/posts', views.PostList.as_view(), name="post_list"),
    path('api/posts/<int:pk>', views.PostDetail.as_view(), name="post_detail"),
]

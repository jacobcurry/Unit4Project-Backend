from django.urls import path
from . import views

urlpatterns = [
    path('api/users', views.UserList.as_view(), name='user_list'), # api/users will be routed to the UserList view for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'), # api/user will be routed to the UserDetail view for handling
]

from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('list/', UserList.as_view(), name='users-list'),
    path('<int:pk>/', UserDetail.as_view(), name='users-detail')
]

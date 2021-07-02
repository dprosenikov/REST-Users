from django.urls import path

from REST_User.users.views import ProfileList, ProfileCreate, ProfileDetailsApiView

urlpatterns = [
    path('', ProfileList.as_view(), name='all users'),
    path('create/', ProfileCreate.as_view(), name='create user'),
    path('<int:pk>/', ProfileDetailsApiView.as_view(), name='user details'),
]

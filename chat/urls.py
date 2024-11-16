from django.urls import path

from chat.views import HomeView, RoomsView, RoomView

app_name = "chat"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('room/', RoomsView.as_view(), name="rooms"),
    path('room/<slug>/', RoomView.as_view(), name="room"),
]

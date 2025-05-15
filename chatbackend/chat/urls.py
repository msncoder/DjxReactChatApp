from django.urls import path
from . import views

urlspatterns = [
    path('rooms/', views.RoomList.as_view()),
    path('rooms/slug:<room_name>/messages/',views.MessageList.as_view())
]
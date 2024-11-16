from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from chat.models import Room, Message


class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        context = {
            "rooms": rooms
        }
        return render(request, "chat/rooms.html", context)


class RoomView(LoginRequiredMixin, View):
    def get(self, request, slug):
        room = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=room)
        context = {
            "room": room,
            "mesages": messages
        }
        return render(request, "chat/room.html", context)
UserCreationForm

class HomeView(TemplateView):
    template_name = "home.html"

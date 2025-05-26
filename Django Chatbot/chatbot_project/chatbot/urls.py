from django.urls import path
from .views import chatbot_response

urlpatterns = [
    path("", chatbot_response, name="chat"),
]
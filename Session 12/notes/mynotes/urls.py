from django.urls import path
from .views import NoteView, NoteDetail

urlpatterns = [
    path('', NoteView.as_view()),
    path('<str:pk>', NoteDetail.as_view())
]
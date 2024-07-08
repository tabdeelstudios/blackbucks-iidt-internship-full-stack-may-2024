from django.urls import path
from .views import BookView, UserCreate

urlpatterns = [
    path('', BookView.as_view()),
    path('regsiter', UserCreate.as_view(), name='user-create')
]
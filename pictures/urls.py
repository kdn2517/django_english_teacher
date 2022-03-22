from django.urls import path
from .views import *

urlpatterns = [
    path('', WordsView.as_view()),
    path('<int:pk>', WordView.as_view()),
]
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Words


class WordsView(ListView):
    model = Words

class WordView(DetailView):
    model = Words

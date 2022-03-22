from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Words


class WordsView(ListView):
    ''' Шаблон words_list.html '''
    model = Words

class WordView(DetailView):
    ''' Шаблон words_detail.html '''
    model = Words

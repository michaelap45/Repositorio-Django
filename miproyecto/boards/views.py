from django.http.response import Http404
from .models import Board
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Board, Topic, Post
from .forms import NewTopicForm
from django.http import JsonResponse

# Create your views here.
def home(req):
    boards = Board.objects.all()
    return render(req,'home.html',{'boards':boards})

def board_topics(req, pk):
    board = get_object_or_404(Board,pk=pk)
    return render(req, 'board_topics.html', {'board' :board })

def new_topic(req,pk):
    board = get_object_or_404(Board,pk=pk)
    user = req.user
    if req.method == 'POST':
        form = NewTopicForm(req.POST)
        if form.is_valid():
            topic = form.save(False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(message = form.cleaned_data.get('message'),topic = topic,created_by = user)
            return redirect('board_topics',pk=pk)
        
    form = NewTopicForm()
    print(form)
    return render(req,'new_topic.html',{'board' : board, 'form':form})

def test(req):
    result = {"name": "Pranay", "class": "4 sem", "college":"Some Raisoni Kindof"}
    return JsonResponse( result )
    
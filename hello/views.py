from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }

    return render(request, 'hello/index.html', params)

def create(request):
    params = {
        'title': 'Hello',
        'form': FriendForm,
    }
    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance = obj)
        friend.save()
        return redirect(to = '/hello')
    
    return render(request, 'hello/create.html', params)
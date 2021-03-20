from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data: ',
            'form': HelloForm(),
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'あなたは、<br>' + request.POST['name'] + '(' + request.POST['age'] + ')<br>さんです。<br>メールアドレスは<br>' + request.POST['mail'] + '<br>ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
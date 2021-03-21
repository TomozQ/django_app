from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from django.db.models import QuerySet

def __new_str__(self):
    result = ''
    for item in self: #item = record
        result += '<tr>'
        for k in item: #k = item.key
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>' #k->key, item[k]->item.key.value
        result += '</tr>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title': 'Hello',
        'data': data,
    }

    return render(request, 'hello/index.html', params)
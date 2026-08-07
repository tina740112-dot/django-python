from django.shortcuts import render
from django.http import HttpResponse

def homework2(request, username):
    #return HttpResponse("Hello, this is homework2!")
    print(f'Username:{username}')
    return render(request, 'show.html',locals())
# Create your views here.

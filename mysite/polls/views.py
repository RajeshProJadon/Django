from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token



# Create your views here.
def index(request):
    return HttpResponse("Hello, World. You're at poll index ")

# ensure_csrf_token(index)
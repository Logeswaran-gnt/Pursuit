from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

#------- DRF ------------
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app_todo.serializers import UserSerializer, GroupSerializer
#------------------------
def login_todo(request):
    print("==============================")
    print(request.user, request.user.is_authenticated)
    print("==========================")
    if request.user.is_authenticated:
        print(request.user, request.user.is_authenticated,'auth')
        return redirect('/home')
    else:
        print(request.user, request.user.is_authenticated,'unauth')
        return render(request, 'app_todo/login.html')

@login_required
def homepage(request):
    return render(request, 'app_todo/dashboard.html')

def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print (user)
        #history(request)
        return redirect('/home')
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

@login_required
def test_logout(request):
    return HttpResponse("Still not logged out")

def logout_todo(request):
    logout(request)
    return redirect('/')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
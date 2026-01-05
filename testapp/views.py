from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='RegularUser')
            user.groups.add(group)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})
def dashboard(request):
    return render(request,'dashboard.html')
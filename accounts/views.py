from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """register a new user"""
    if request.method != 'POST':
        #Display Blank form
        form = UserCreationForm()

    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            #register the user and redirect the user
            login(request,new_user)
            return redirect('learnLogs:index')

    context = {'form':form}
    return render(request,'registration/register.html',context)



from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import myUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from langchains.llmmodels import llminput


@login_required(login_url='login')
def home(request):

    if request.method=="GET":
        return render (request,'index.html')
    else:
        query=request.POST.get('query')
        index=llminput()
        results=index.query(query)
        
        data={"query":"you aksed : "+" "+query+" "+"?","response":"Ans : "+" "+results}
        return render (request,'index.html',data)

class SignUpView(generic.CreateView):
    form_class = myUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    
    
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'account done not exit plz sign in')
    # form = AuthenticationForm()
    return render(request, 'login.html')
def Logout(request):
    logout(request)
    return redirect('/login')
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render,redirect
from onlineapp.forms import SignupForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import logout


def log_out(request):
    logout(request)
    return redirect('login')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(
            request,
            template_name='log_in.html',
            context={'form': form}
        )
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('colleges')
        else:
            messages.error(request,'Invalid Babai, malli chudu')


class SignupView(View):
    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return render(
            request,
            template_name='signup.html',
            context={'form': form}
        )
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(**form.cleaned_data)

                if user is not None:
                    login(request,user)
                    return redirect('colleges')
                else:
                    #messages.error(request, 'Invalid Babai, malli chudu')
                    return redirect('signup')

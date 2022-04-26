from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        # veritabanına kayıt islemi
        newUser = User(username = username, email = email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser) # veritabanına kaydeder ve giris yapar
        
        messages.success(request, message = 'Başarıyla Kayıt Oldunuz.')
        return redirect('index')
        
    context = {'form': form}
    return render(request, 'register.html', context)
    
def loginUser(request):
    form = LoginForm(request.POST or None)
    
    context = {'form': form}
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, message = 'Kullanıcı adı veya parola hatalı!')
            return render(request, 'login.html', context)
        
        messages.success(request, message = 'Başarıyla giriş yaptınız.')
        login(request, user)
        return redirect('index')
    
    return render(request, 'login.html', context)    

def logoutUser(request):
    logout(request)
    messages.warning(request, message = 'Başarıyla çıkış yaptınız.')
    return redirect('index')
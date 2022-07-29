from django.shortcuts import render, redirect
from django.contrib import auth
from .models import People
from .forms import PeopleForm

def login(request):
    nickname = People.objects.all()
    
    return render(request, 'login.html',{'nickname':nickname})

# def kakao_login(request):
#     client_id = 'eafa367a0c6119d491faf41d932dfcc7'
#     redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
#     return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")


# def kakao_login(request):
#     client_id = 'eafa367a0c6119d491faf41d932dfcc7'
#     redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
#     return redirect('nickname')

def done(request):
    return render(request, 'done.html')

def user(request):
    return render(request, 'name.html')

def nickname(request):
    if request.method == 'POST':
        myname = request.POST['myname']
        form = PeopleForm(request.POST, request.FILES)
        if form.is_valid():
            name = People()
            name.person = form.cleaned_data['person']
            name.save()
            return redirect('login')
    else:
        form = PeopleForm()
    return render(request, 'login.html', {'form':form})
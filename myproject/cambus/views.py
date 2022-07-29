from django.shortcuts import render, redirect
from .models import Register
from .forms import RegisterForm

def home(request): #홈/달력
    return render(request, 'index.html')


def answer(request):    #답록
    return render(request, 'answer.html')


def question(request):  #질문등록
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            post = Register()
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'question.html', {'form':form})

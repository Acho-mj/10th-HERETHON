from django.contrib import admin
from django.urls import include, path
from cambus import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #cambus
    path('answer/', views.answer, name="answer"),
    path('question/', views.question, name="question"),
    
    #계정
    path('', accounts_views.login, name='login'),
    path('user', accounts_views.user, name='user'),
    path('nickname/', accounts_views.nickname, name='nickname'),
    path('done', accounts_views.done, name='done'),
    #카카오 로그인
    path('accounts/', include('allauth.urls')),
    # path('account/login/kakao/', accounts_views.kakao_login),
]

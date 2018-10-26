from django.shortcuts import render
from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email', False)

		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None:
			message = '此使用者已經有人使用'
		else:
			user = User.objects.create_user(username, email, password)
			user.save()
			message = "註冊成功"
			return redirect('/login/')
	return render(request, 'register.html', locals())

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				message = '登入成功!'
				return redirect('/hello/')
			else:
				message = '帳號尚未啟用!'
		else:
			message = '登入失敗!'
	return render(request,"login.html",locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('//')

def hello(request):
    return render(request, 'hello.html',locals())
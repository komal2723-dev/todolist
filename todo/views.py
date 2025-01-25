from django.shortcuts import render,redirect
from . forms import registraitonform,AuthenticationForm

from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
	return render(request,'todo/home.html')


def register(request):
	if request.method=='POST':
		form = registraitonform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form=registraitonform()
	
	return render(request,'todo/signup.html',{"form":form})
		
def user_login(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = AuthenticationForm(request=request, data = request.POST)
			if form.is_valid():
				username = form.cleaned_data.get("username")
				password = form.cleaned_data.get("password")
				user = authenticate(username=username,password=password)
				if user is not None:
					login(request,user)
					return redirect('todopage')
		else:
			form = AuthenticationForm()
		return render(request,"todo/login.html",{'form':form})
	else:
		return redirect('todopage')




def todopage(request):
	if request.user.is_authenticated:
		return render(request,'todo/todopage.html', {'name': request.user})
	else:
		return redirect('login')

def user_logout(request):
	logout(request)
	return redirect('login')
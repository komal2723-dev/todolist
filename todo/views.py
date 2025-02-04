from django.shortcuts import render,redirect
from . forms import registraitonform,AuthenticationForm, TodoForm, ForgotPasswordForm, verifycodeform, setPasswordForm
from . models import Task
from django.contrib import messages
from django.contrib.auth.models import User	
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.hashers import make_password
import secrets
import string

# Create your views here.
def register(request):
	if request.method=='POST':
		form = registraitonform(request.POST)
		get_all_users_by_username = User.objects.all().filter(username=form.data['username'])
		if get_all_users_by_username.exists():
			messages.error(request, f'Username already exists!')
			return redirect('signup') 
		if form.is_valid():
			form.save()
			messages.success(request, f'Account created successfully for {form.cleaned_data["username"]}')
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
					messages.error(request,f"Invalid username or password")
					return redirect('login')
		else:
			form = AuthenticationForm()
		return render(request,"todo/login.html",{'form':form})
	else:
		return redirect('todopage')

def todopage(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			form = TodoForm(request.POST)
			if form.is_valid():
				task = form.save(commit=False)
				task.user = request.user
				task.save()
				result = Task.objects.filter(user=request.user)
				form = TodoForm()
		else:
			form = TodoForm()
			result = Task.objects.filter(user=request.user)
		return render(request,'todo/todopage.html', {'name': request.user, 'result':result,'form':form})
		
	else:
		return redirect('login')

def user_logout(request):
	logout(request)
	return redirect('login')

def edit_todolist(request,task_id):
	if request.method=="POST":
		todo = Task.objects.get(pk = task_id)
		form = TodoForm(request.POST, instance = todo)
		if form.is_valid():
			form.save()
			messages.success(request,f'Task Updated Successfully!!')
			return redirect('todopage')
	else:
		todo = Task.objects.get(pk = task_id)
		form = TodoForm(instance = todo)
	return render(request,'todo/edit_todolist.html',{'form':form})

def delete_task(request,task_id):
	todo = Task.objects.get(pk = task_id)
	todo.delete()
	return redirect('todopage')


# FUNCTION TO GENERATE OTP
def generate_otp(length = 6):
	otp = ''.join(secrets.choice(string.digits) for i in range(length))
	return otp


# VIEW TO SEND OTP TO EMAIL

def send_otp(request):
	if request.method == 'POST':
		form = ForgotPasswordForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			if User.objects.filter(email=email).exists():
			#Generate OTP and store it in session
				otp = generate_otp()

				# store otp into session
				request.session['otp'] = otp
				request.session['email'] = email
				# send otp via email
				send_mail(
					'Your OTP Code',
					f'Your OTP Code is {otp}',
					settings.EMAIL_HOST_USER,
					[email],
					fail_silently=True
				)
				messages.success(request, f'OTP sent to {email}. Please check your inbox.')
				return HttpResponseRedirect('/verify-otp/')  # Redirect to the verification page
			else:
				messages.error(request, f'No account found with this email address.')
				return redirect('login')
	else:
		form = ForgotPasswordForm()

	return render(request, 'todo/send_otp.html', {'form': form})

# otp verification view

def verify_otp(request):
	if request.method == 'POST':
		entered_otp = verifycodeform(request.POST)
		if entered_otp.is_valid():
			entered_otp = entered_otp.cleaned_data['code']
			print(entered_otp)
			stored_otp = request.session.get('otp')
			if entered_otp == stored_otp:
				messages.success(request, 'OTP verified successfully!')
				return redirect('set_password')
			else:
				messages.error(request,"Invalid OTP. Please try again.")
				return redirect('verify_otp')
	else:
		entered_otp = verifycodeform()
		return render(request, 'todo/verify_otp.html',{'form':entered_otp})
	
def set_password(request):
	if request.method == 'POST':
		form = setPasswordForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data['new_password1']
			hashed_password = make_password(password)
			User.objects.filter(email=request.session.get('email')).update(password=hashed_password)
			messages.success(request, 'Password updated successfully!')
			return redirect('login')
	else:
		form = setPasswordForm()
	return render(request,'todo/set_password.html',{'form':form})
	
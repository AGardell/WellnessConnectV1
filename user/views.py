from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import Member
from .forms import SignUpForm

# Create your views here.
def Login(request):
    if (request.method == 'POST'):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if (user is not None):
            login(request, user)
            messages.success(request, f"Welcome {user.first_name}")
            return render(request, 'search/base.html')
        else:
            messages.error(request, "Invalid Username and/or Password. Please try again.")
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, 'search/base.html')

def Signup(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)

        if (form.is_valid):
            user = User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password'))
            user.first_name = request.POST.get("firstName")
            user.last_name = request.POST.get("lastName")
            user.member.address_1 = request.POST.get("address_1")
            user.member.address_2 = request.POST.get("address_2")
            user.member.city = request.POST.get("city")
            user.member.state = request.POST.get("state")
            user.member.zip = request.POST.get("zipcode")
            user.save()
            messages.add_message(request, messages.SUCCESS, f"Welcome {user.first_name}! Your account has been created, please log in now!")
            return render(request, 'user/login.html')
        else:
            return render(request, 'user/signup.html', {'form':form})
    else:
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form':form}) 
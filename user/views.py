from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Member

# Create your views here.
def Login(request):
    return render(request, 'user/login.html')

def Signup(request):
    if (request.method == 'POST'):

        user = User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password'))
        user.first_name = request.POST.get("firstname")
        user.last_name = request.POST.get("lastname")
        user.member.address_1 = request.POST.get("address1")
        user.member.address_2 = request.POST.get("address2")
        user.member.city = request.POST.get("city")
        user.member.state = request.POST.get("state")
        user.member.zip = request.POST.get("zip")
        user.save()

        return render(request, 'user/signup.html')
    else:
        return render(request, 'user/signup.html')
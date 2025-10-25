from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from base.models import employess
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_(request):
    if request.method=='POST':
        usernamed=request.POST['u_name']
        pas=request.POST['p_name']
        u=authenticate(username=usernamed,password=pas)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':"Wrong Credentials........"})
    return render (request,'login.html')

def register(request):
    if request.method=='POST':
        first_named=request.POST['f_name']
        lastname_named=request.POST['l_name']
        emaild=request.POST['e_name']
        usernamed=request.POST['u_name']
        pas=request.POST['p_name']
        u=authenticate(username=usernamed,password=pas)
        if u:
                return render(request,'register.html',{'msg':'This is credintials are there'})
        else:
            u=User.objects.create(first_name=first_named,last_name=lastname_named,email=emaild,username=usernamed)
            u.set_password(pas)
            u.save()
            return redirect('home')
                
    return render(request,'register.html')

def logout_(request):
    # u=User.objects.get(username=request.user)
    # u.delete()
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    print("View hit!")
    print(request.user)
    try:
        e = employess.objects.get(email=request.user.email)
        if not e.user:
            e.user = request.user
            e.save()
    except employess.DoesNotExist:
        e = None
    return render(request, 'profile.html', {'e': e})
    



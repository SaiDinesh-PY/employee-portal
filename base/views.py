from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import talks,notifications,employess
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from django.db.models import Q
import pickle
import numpy as np
# import os
# Create your views here.
@login_required(login_url='login')
def home(request):
    s=talks.objects.all()
    return render(request, 'home.html',{'data':s})

@login_required(login_url='login')
def talk(request):
    return render(request, 'talk.html')

@login_required(login_url='login')
def add_talk(request):
    if request.method=='GET' and 'title' in request.GET and 'description' in request.GET:
        titled=request.GET['title']
        descd=request.GET['description']
        talks.objects.create(title=titled,desc=descd,user=request.user)
        return redirect('home')
    return render(request,'add_talk.html')

@login_required(login_url='login')
def my_notifications(request):
    a= notifications.objects.filter(Q(From=request.user.username) | Q(to=request.user.username))
    # a=notifications.objects.all()
    try:
        for i in a:
            u=User.objects.get(username=i.From)
            i.user=u
            i.save()
    except:
        print(a)
    # for i in a:
        # i.delete()
    return render(request, 'notify.html', {'data': a})



@login_required(login_url='login')
def sender(request,pk):
    s=notifications.objects.get(id=pk)
    if request.method=='POST':
        to_user=request.POST['to']
        message=request.POST['message']
        from_user=request.user.username
        notifications.objects.create(From=from_user, to=to_user, message=message)
        return redirect('home')
    return render(request,'sender.html',{'data':s})

def send(request):
    e=employess.objects.get(email=request.user.email)
    if request.method=='POST':
        to_user=request.POST['to']
        message=request.POST['message']
        from_user=request.user.username
        notifications.objects.create(From=from_user, to=to_user, message=message)
        return redirect('home')
    return render(request,'send.html',{'data':e})

@login_required(login_url='login')
def addco(request):
    if request.method=='POST':
        print("hi")
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmployeeForm()
    return render(request,'addco.html',{'form':form})

@login_required(login_url='login')
def colleagues(request):
    e=employess.objects.all()
    return render(request,"colleagues.html",{'data':e})

@login_required(login_url='login')
def checkit(request):
    if 'satisfaction_level' in request.GET:
        satisfaction_level=request.GET['satisfaction_level']
        last_evaluation=request.GET['last_evaluation']
        number_project=request.GET['number_project']
        average_montly_hours=request.GET['average_montly_hours']
        time_spend_company=request.GET['time_spend_company']
        f=open("turnover.pkl","rb")
        mp=pickle.load(f)
        salary={0:'low',1:'medium',2:'high'}
        v=mp.predict(np.array([[satisfaction_level,last_evaluation,number_project,average_montly_hours,time_spend_company]]))
        if satisfaction_level and last_evaluation and number_project and average_montly_hours and time_spend_company:

        # Convert input types (IMPORTANT)
            satisfaction_level = float(satisfaction_level)
            last_evaluation = float(last_evaluation)
            number_project = int(number_project)
            average_montly_hours = int(average_montly_hours)
            time_spend_company = int(time_spend_company)

            f = open("turnover.pkl", "rb")
            mp = pickle.load(f)

            salary = {0: 'low', 1: 'medium', 2: 'high'}
            v = mp.predict(np.array([[satisfaction_level,
                                    last_evaluation,
                                    number_project,
                                    average_montly_hours,
                                    time_spend_company]]))[0]

            # Conditions
            salary = {0: 'low', 1: 'medium', 2: 'high'}
            salary_level = salary[v]  # prediction mapped once ✅

            if v==2:
                d=f"you can have chance of getting promtion and salary goes to {salary_level}"
                return render(request, 'check.html', {'data': d, 'color': 'green'})
            elif v==1:
                d=f"if you are near to get promotion and now you salary goes to {salary_level}"
                return render(request, 'check.html', {'data': d, 'color': 'yellow'})
            elif v==0:
                d=f"your job at risk and your salary goes to {salary_level}"
                return render(request, 'check.html', {'data': d, 'color': 'red'})

                    # First load (form only, empty message)
    return render(request, 'check.html', {'data': None, 'color': 'black'})

def about(request):
    return render(request,'about.html')
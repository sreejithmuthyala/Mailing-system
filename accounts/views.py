# from curses.ascii import HT
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Sentreceive
from datetime import datetime

# from django.db import Sent

# Create your views here.
# @register.filter(name='split')
# def split(value, key):
#     """
#         Returns the value turned into a list.
#     """
#     return value.split(key)
    
def lore(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # receive_mails = Sentreceive.objects.filter(username=username).values_list('receive_mails')
            # myreceived=list(receive_mails[0][0])
            # myreceived=tuple(myreceived)
            print(datetime.now())
            rm = Sentreceive.objects.filter(username=username).values_list('rm')
            if len(rm[0][0])==0:
                rm1='No mails to display'
                print(rm1)
                return render(request,'inbox.html',{'rm2':rm1})
            rm1= list(rm[0][0])
            rm1.reverse()
            return render(request,'inbox.html', {'rm':rm1})
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email=request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
            
        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name )
                mails = Sentreceive.objects.create(username=username, rm=[], sm=[])
                mails.save()
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def sent(request):
    current_user=request.user
    sm=Sentreceive.objects.filter(username=current_user.username).values_list('sm')
    if len(sm[0][0])==0:
        sm1='No Sent mails to display'
        return render(request,'sent.html',{'sm2':sm1})
    sm1=list(sm[0][0])
    sm1.reverse()
    return render(request, 'sent.html',{'sm':sm1})


def compose(request):
    return render(request, 'compose.html')

def inbox(request):
    if request.method == 'POST':
        username = request.POST['username']
        body = request.POST['body']
        subject = request.POST['subject']
        l=[body]
        
        current_user = request.user

        l=[]
        time = datetime.now()
        formatedDate = time.strftime("%Y-%m-%d %H:%M")
        l.append(formatedDate)
        l.append(current_user.username)
        l.append(subject)
        l.append(body)
        # print(l)
        print(username)
        print(current_user.username)
        rm = Sentreceive.objects.filter(username=username).values_list('rm')
        # print(rm)
        # if len(rm[0][0])==0:
        #     rm2=[l]
        #     print(rm2)
        #     Sentreceive.objects.filter(username=username).update(rm=rm2)
        # else:
        rm1= list(rm[0][0])
        rm1.append(l)
        print(rm1)
        Sentreceive.objects.filter(username=username).update(rm=rm1)
        
        
        # print(rm1)
        
        m=[]
        m.append(formatedDate)
        m.append(username)
        m.append(subject)
        m.append(body)
        sm = Sentreceive.objects.filter(username=current_user.username).values_list('sm')
        # if len(sm[0][0])==0:
        #     sm2=[m]
        #     Sentreceive.objects.filter(username=current_user.username).update(sm=sm2)
        # else:
        sm1 = list(sm[0][0])
        sm1.append(m)
        Sentreceive.objects.filter(username=current_user.username).update(sm=sm1)
        # receive_mails = Sentreceive.objects.filter(username=current_user.username).values_list('receive_mails')
        # myreceived=list(receive_mails[0][0])
        # myreceived=tuple(myreceived)
        rm = Sentreceive.objects.filter(username=current_user.username).values_list('rm')
        if len(rm[0][0])==0:
                rm1='No mails to display'
                print(rm1)
                return render(request,'inbox.html',{'rm2':rm1})
        rm1= list(rm[0][0])
        rm1.reverse()

        return render(request,'inbox.html',{'rm':rm1})
    
    else:

        return redirect('login')
    

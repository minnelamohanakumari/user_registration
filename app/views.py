from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.core.mail import send_mail
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            NSUO.set_password(ufd.cleaned_data['password'])
            NSUO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail('registration',
            'registration is successfull',
            'minnelamohanakumari18@gmail.com',
            [NSUO.email],
            fail_silently=True
            )
            return HttpResponse('registration is succesfull')
        else:
            return HttpResponse('data is invalid')
    return render(request,'registration.html',d)
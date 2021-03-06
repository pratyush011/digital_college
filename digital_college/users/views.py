from django.shortcuts import render
from django.forms import ModelForm
from .models import Registered_User,Registered_College
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


class User_Registration_Form(ModelForm):
    ROLE_CHOICES=(
        ('F','Faculty'),
        ('S','Student')
    )
    role=forms.ChoiceField(choices=ROLE_CHOICES)
    college_id=forms.ModelChoiceField(queryset=Registered_College.objects.all())
    class Meta:
        model=Registered_User
        fields=['email','role','college_id','activation_key',]

class College_Registration_Form(ModelForm):
    STATE_CHOICES=(
        ('AP','Andhra Pradesh'),
        ('AC','Arunchal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('CH','Chattisgarh'),
        ('GO','Goa'),
        ('GJ','Gujarat'),
        ('HR','Haryana'),
        ('HP','Himachal Pradesh'),
        ('JK','Jammu and Kashmir'),
        ('JH','Jharkhand'),
        ('KN','Karnataka'),
        ('KL','Kerala'),
        ('MP','Madhya Pradesh'),
        ('MH','Maharastra'),
        ('MN','Manipur'),
        ('MZ','Mizoram'),
        ('MG','Meghalaya'),
        ('NG','Nagaland'),
        ('OR','Orissa'),
        ('PB','Punjab'),
        ('RJ','Rajasthan'),
        ('SK','Sikkim'),
        ('TN','Tamil Nadu'),
        ('TG','Telangana'),
        ('TP','Tripura'),
        ('UL','Uttaranchal'),
        ('UP','Uttar Pradesh'),
        ('WB','West Bengal')
    )
    Password=forms.CharField(widget=forms.PasswordInput)
    Email_Id=forms.CharField(widget=forms.EmailInput)
    State=forms.ChoiceField(choices=STATE_CHOICES)
    class Meta:
        model=Registered_College
        fields=['Name_Of_College','Password','Email_Id','College_Registration_Number',
        'City','State']

def User_Registration(request):
    forms={}
    if request.method == 'POST':
        forms['User_Creation_Form']=UserCreationForm(request.POST)
        forms['User_Registration_Form']=User_Registration_Form(request.POST)
        if forms['User_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            current_user=forms['User_Creation_Form'].save(commit=False)
            username=forms['User_Creation_Form'].cleaned_data.get('username')
            password=forms['User_Creation_Form'].cleaned_data.get('password1')
            user=current_user
            user.save()
            email=forms['User_Registration_Form'].cleaned_data.get('email')
            role=forms['User_Registration_Form'].cleaned_data.get('role')
            college_id=forms['User_Registration_Form'].cleaned_data.get('college_id')
            activation_key=forms['User_Registration_Form'].cleaned_data.get('activation_key')
            current_user=Registered_User(user=user,email=email,role=role,college_id=college_id,activation_key=activation_key)
            current_user.save()
            return redirect('User_Home')
    else:
        forms['User_Registration_Form'] = User_Registration_Form()
        forms['User_Creation_Form'] = UserCreationForm()
    return render(request,'users/User_Registration.html',{'forms':forms})



def College_Registration(request):
    if request.method == 'POST':
        form =  College_Registration_Form(request.POST)
        if form.is_valid():
            print('hello')
            form.save()
            return redirect('College_Home')
    else:
        form = College_Registration_Form()
    return render(request,'users/College_Registration.html',{'form':form})

def User_Home(request):
    classrooms=['cs1','cs2','cs3']
    clubs=['cb1','cb2','cb3']
    context = {
        'classrooms':classrooms,
        'clubs':clubs
    }
    return render(request,'users/user_home.html',context)

def College_Home(request):
    return render(request,'users/college_home.html')

def website_homepage(request):
    return render(request,'users/website_homepage.html')

def website_register(request):
    return render(request,'users/website_register.html')
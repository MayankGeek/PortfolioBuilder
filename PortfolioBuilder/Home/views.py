from django.shortcuts import render,HttpResponse,redirect
from .forms import UserInfoForm
from django.contrib.auth.decorators import login_required
from Home.models import UserInfo
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
    
@login_required
def get_details_form(request):
    try:
        if request.method=="POST":
            form=UserInfoForm(request.POST,request.FILES)
            if form.is_valid():
                name=form.cleaned_data.get('name')
                email=form.cleaned_data.get('email')
                mobile_no=form.cleaned_data.get('mobile_no')
                place=form.cleaned_data.get('place')
                profession=form.cleaned_data.get('profession')
                about=form.cleaned_data.get('about')
                profile_picture=form.cleaned_data.get('profile_picture')
                user=UserInfo.objects.create(user=request.user,
                name=name,
                email=email,
                mobile_no=mobile_no,
                place=place,
                profession=profession,
                about=about,
                profile_picture=profile_picture,
                )
                user.slug_save()
                messages.success(request,"Please check your details you have provided press update to update if you entered anything wrong")
                return redirect('Home:details_page', slug=user.get_slug())
        else:
            form=UserInfoForm()
        return render(request,'get_details_form.html',{form:form})
    except:
        return HttpResponse("something went wrong")


def details_page(request,slug):
    return render(request,'details_page.html')

def add_skills_form(request):
    return render(request,'add_skills_form.html')

def skill_details_page(request):
    return render(request,'skill_details.html')

def add_education_form(request):
    return render(request,'add_education_form.html')

def education_details_page(request):
    return render(request,'education_details.html')

def add_expertise_form(request):
    return render(request,'add_expertise_form.html')

def expertise_details_page(request):
    return render(request,'expertise_details.html')

def add_experience_form(request):
    return render(request,'add_experience_form.html')

def experience_details_page(request):
    return render(request,'experience_details.html')

def add_project_form(request):
    return render(request,'add_project_form.html')

def project_details_page(request):
    return render(request,'project_details.html')


from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def get_details_form(request):
    return render(request,'get_details_form.html')

def details_page(request):
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
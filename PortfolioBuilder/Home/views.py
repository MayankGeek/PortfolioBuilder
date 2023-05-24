from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserInfoForm,AddSkillForm
from django.contrib.auth.decorators import login_required
from Home.models import UserInfo,Skill
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

@login_required
def details_page(request,slug):
    context={}
    context['details_page']=UserInfo.objects.get(slug=slug)
    return render(request,'details_page.html',context)

@login_required
def change_info(request, slug):
    obj=get_object_or_404(UserInfo,slug=slug)
    form=UserInfoForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"your information has been updated")
        return redirect("Home:details_page",slug=slug)
    form=UserInfoForm(request.POST and request.FILES or None,instance=obj)
    return render(request,"change_info.html",{"form":form})

# def add_skills_form(request,slug):

#     if request.method=="POST":
#         form=AddSkillForm(request.POST)
#         slug=UserInfo.objects.get(user=request.user,slug=slug)
#         if form.is_valid():
#             skill=form.cleaned_data.get('skill')
#             percent=form.cleaned_data.get('percent')
#             skill2=form.cleaned_data.get('skill2')
#             percent2=form.cleaned_data.get('percent2')
#             if not Skill.objects.filter(user=request.user,slug__slug=slug,skill=skill,percent=percent,skill2=skill2,percent2=percent2):
#                 skills=Skill(user=request.user,slug=slug,skill=skill,percent=percent,skill2=skill2,percent2=percent2)
#                 skills.save()
#                 messages.success(request, "your skilles has been saved")
#                 return redirect("Home:skill_details_page",slug=slug)
#             else:
#                 messages.error(request, "You filled wrong information")
#     form = AddSkillForm()
#     return render(request, "add_skills_form.html", {'form': form, 'slug': slug})
    # return render(request,'add_skills_form.html')
# def add_skills_form(request, slug):
#     slug_obj = UserInfo.objects.get(user=request.user, slug=slug)
#     if request.method == "POST":
#         form = AddSkillForm(request.POST)
#         if form.is_valid():
#             skill1 = form.cleaned_data.get('skill1')
#             percent1 = form.cleaned_data.get('percent1')
#             # skill2 = form.cleaned_data.get('skill2')
#             # percent2 = form.cleaned_data.get('percent2')

#             # Check if the skill combination already exists for the user and slug
#             if not Skill.objects.filter(user=request.user, slug__slug=slug, skill1=skill1, percent1=percent1):
#                 skills = Skill(user=request.user, slug=slug_obj, skill1=skill1, percent1=percent1)
#                 skills.save()
#                 messages.success(request, "Your skills have been saved.")
#                 return redirect("Home:skill_details_page", slug=slug)
#             else:
#                 messages.error(request, "You entered wrong information.")
#     else:
#         form = AddSkillForm()
    
#     return render(request, "add_skills_form.html", {'form': form, 'slug': slug})

#testing code for add_skills_form
@login_required
def add_skills_form(request, slug):
    if request.method == "POST":

        form = AddSkillForm(request.POST)
        slug = UserInfo.objects.get(user=request.user, slug=slug)
        if form.is_valid():
            skill1 = form.cleaned_data.get('skill1')
            # skill1 = skill.capitalize()
            percent1 = form.cleaned_data.get('percent1')
            skill2 = form.cleaned_data.get('skill2')
            # skill1 = skill.capitalize()
            percent2 = form.cleaned_data.get('percent2')
            skill3 = form.cleaned_data.get('skill3')
            # skill1 = skill.capitalize()
            percent3 = form.cleaned_data.get('percent3')
            skill4 = form.cleaned_data.get('skill4')
            # skill1 = skill.capitalize()
            percent4 = form.cleaned_data.get('percent4')
            skill5 = form.cleaned_data.get('skill5')
            # skill1 = skill.capitalize()
            percent5 = form.cleaned_data.get('percent5')
            if not Skill.objects.filter(user=request.user, slug__slug=slug,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,skill5=skill5):
                skills = Skill(user=request.user, slug=slug, skill1=skill1, percent1=percent1,skill2=skill2,percent2=percent2,skill3=skill3,
                percent3=percent3,skill4=skill4,percent4=percent4,skill5=skill5,percent5=percent5)
                skills.save()
                messages.success(request, "Your skill is registered")
                return redirect('Home:skill_details_page', slug=slug)
            else:
                return HttpResponse("<h3>You already have registered this skill"
                                        " go and edit if you want......go back</h3>")
    form = AddSkillForm()
    return render(request, "add_skills_form.html", {'form': form, 'slug': slug})

@login_required
def skill_details_page(request,slug):
    details = Skill.objects.filter(slug__slug=slug).all()
    return render(request, 'skill_details.html', {'details': details, 'slug': slug})

  

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

# @login_required
# def user_portfolios(request):
#     context={}
#     context['user_portfolios']=UserInfo.objects.filter(user=request.user).all()
#     return render(request,'user_portfolios.html',context)

@login_required
def user_portfolios(request):
    context = {}
    portfolios = UserInfo.objects.filter(user=request.user).all()
    
    if not portfolios:
        # context['message'] = "No portfolios created."
        messages.success(request,"You don't any portfolios created please create one now !")
    
    context['user_portfolios'] = portfolios
    return render(request, 'user_portfolios.html', context)


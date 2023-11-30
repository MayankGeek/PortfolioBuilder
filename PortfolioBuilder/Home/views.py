from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserInfoForm,AddSkillForm,EducationForm,ExperienceForm,ProjectForm
from django.contrib.auth.decorators import login_required
from Home.models import UserInfo,Skill,Education,Experience,Project
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
                linkedin_url=form.cleaned_data.get('linkedin_url')
                user=UserInfo.objects.create(user=request.user,
                name=name,
                email=email,
                mobile_no=mobile_no,
                place=place,
                profession=profession,
                about=about,
                profile_picture=profile_picture,
                linkedin_url=linkedin_url,
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

# @login_required
# def change_info(request, slug):
#     obj=get_object_or_404(UserInfo,slug=slug)
#     form=UserInfoForm(request.POST or None,request.FILES,instance=obj)
#     if form.is_valid():
#         form.save()
#         messages.success(request,"your information has been updated")
#         return redirect("Home:details_page",slug=slug)
#     form=UserInfoForm(request.POST and request.FILES or None,instance=obj)
#     return render(request,"change_info.html",{"form":form})


#working code for the linkedin problem 
@login_required
def change_info(request, slug):
    obj = get_object_or_404(UserInfo, slug=slug)
    if request.method == "POST":
        form = UserInfoForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Your information has been updated")
            return redirect("Home:details_page", slug=slug)
    else:
        form = UserInfoForm(instance=obj)

    return render(request, "change_info.html", {"form": form, "slug": slug})



#testing code for add_skills_form
@login_required
def add_skills_form(request, slug):
    if request.method == "POST":

        form = AddSkillForm(request.POST)
        slug = UserInfo.objects.get(user=request.user, slug=slug)
        if form.is_valid():
            skill = form.cleaned_data.get('skill')
            percent = form.cleaned_data.get('percent')
            if not Skill.objects.filter(user=request.user, slug__slug=slug,skill=skill):
                skills = Skill(user=request.user, slug=slug, skill=skill, percent=percent)
                skills.save()
                messages.success(request, "Your skill is registered")
                details = Skill.objects.filter(slug__slug=slug).all()
                return render(request, 'add_skills_form.html', {'details': details, 'slug': slug})
            else:
                messages.success(request,"You already have that skill added")
    form = AddSkillForm()
    return render(request, "add_skills_form.html", {'form': form, 'slug': slug})

@login_required
def skill_details_page(request,slug):
    details = Skill.objects.filter(slug__slug=slug).all()
    # print(details)
    return render(request, 'skill_details.html', {'details': details, 'slug': slug})

  
# @login_required
# def add_education_form(request):
@login_required
def add_education_form(request, slug):
    if request.method == "POST":
        form = EducationForm(request.POST)
        slug = UserInfo.objects.get(user=request.user, slug=slug)
        if form.is_valid():
            board_or_univ = form.cleaned_data.get('board_or_univ')
            course = form.cleaned_data.get('course')
            cgpa_or_percent=form.cleaned_data.get('cgpa_or_percent')
            cgpa=form.cleaned_data.get('cgpa')
            add_education=Education(user=request.user,
                                slug=slug,
                                board_or_univ=board_or_univ,
                                course=course,
                                cgpa_or_percent=cgpa_or_percent,
                                cgpa=cgpa
                                )
            add_education.save()
            messages.success(request, "Education details is registered")
            # return render(request, 'education_details_page.html',slug=slug)
            # return redirect('Home:education_details_page',slug=slug)
            # details = Skill.objects.filter(slug__slug=slug).all()
            education_details=Education.objects.filter(slug__slug=slug).all()
            return render(request,'add_education_form.html',{'education_details':education_details,'slug':slug})
        
        else:
            messages.success(request,"something went wrong")
    form = EducationForm()
    return render(request, "add_education_form.html", {'form': form, 'slug': slug})

    return render(request,'add_education_form.html')
@login_required
def education_details_page(request,slug):
    education_details=Education.objects.filter(slug__slug=slug).all()
    return render(request,'education_details.html',{'education_details':education_details,'slug':slug})


def add_expertise_form(request):
    return render(request,'add_expertise_form.html')

def expertise_details_page(request):
    return render(request,'expertise_details.html')

@login_required
def add_experience_form(request,slug):
    try:
        if request.method=="POST":
            form=ExperienceForm(request.POST)
            slug=UserInfo.objects.get(user=request.user,slug=slug)
            if form.is_valid():
                organisation_name=form.cleaned_data.get('organisation_name')
                position=form.cleaned_data.get('position')
                joining_date=form.cleaned_data.get('joining_date')
                ending_date=form.cleaned_data.get('ending_date')
                work_experience=form.cleaned_data.get('work_experience')
                add_experience=Experience(user=request.user,
                                          slug=slug,
                                          organisation_name=organisation_name,
                                          position=position,
                                          joining_date=joining_date,
                                          ending_date=ending_date,
                                          work_experience=work_experience
                )
                add_experience.save()
                messages.success(request,"Experience added successfully")
                experience_details=Experience.objects.filter(slug__slug=slug).all()
                return render(request,"add_experience_form.html",{'experience_detail':experience_details,'slug':slug})
            else:
                messages.success("Something went wrong")
        form=ExperienceForm()
        return render(request,"add_experience_form.html",{'form':form,'slug':slug})
    except:
        messages.success("we are facing some issue!")

def experience_details_page(request,slug):
    experience_details=Experience.objects.filter(slug__slug=slug).all()
    return render(request,"experience_details.html",{'experience_details':experience_details,'slug':slug})

@login_required
def add_project_form(request,slug):
    try:
        if request.method=="POST":
            form=ProjectForm(request.POST)
            slug=UserInfo.objects.get(user=request.user,slug=slug)
            if form.is_valid():
                project_name=form.cleaned_data.get('project_name')
                project_desc=form.cleaned_data.get('project_desc')
                project_start_date=form.cleaned_data.get('project_start_date')
                project_end_date=form.cleaned_data.get('project_end_date')
                project_link=form.cleaned_data.get('project_link')
                add_project=Project(user=request.user,
                                    slug=slug,
                                    project_name=project_name,
                                    project_desc=project_desc,
                                    project_start_date=project_start_date,
                                    project_end_date=project_end_date,
                                    project_link=project_link
                                    )
                add_project.save()
                messages.success(request,"Project added successfully")
                project_details=Project.objects.filter(slug__slug=slug).all()
                return render(request,"add_project_form.html",{'project_details':project_details,'slug':slug})
            else:
                messages.success("somethin went wrong")
        form=ProjectForm()
        return render(request,"add_project_form.html",{'form':form,'slug':slug})
    except:
        messages(request,"We are facing some issues")
    # return render(request,'add_project_form.html')
@login_required
def project_details_page(request,slug):
    project_details=Project.objects.filter(slug__slug=slug).all()
    return render(request,"project_details.html",{'project_details':project_details,'slug':slug})
    # return render(request,'project_details.html')

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

@login_required
def update_skill(request,slug,skill):

    obj = get_object_or_404(Skill,user=request.user, slug__slug=slug, skill=skill)
    form = AddSkillForm(request.POST or None, instance=obj)
    if form.is_valid():
        skill = form.cleaned_data.get('skill')
        percent = form.cleaned_data.get('percent')
        form.save()
        messages.success(request, "Your skill is updated")
        return redirect('Home:skill_details_page', slug=slug)

    form = AddSkillForm(request.POST or None, instance=obj)
    return render(request, "update_skill.html", {'form': form})

@login_required
def delete_skill(request,slug,skill):
    obj=Skill.objects.filter(user=request.user,slug__slug=slug,skill=skill)
    obj.delete()
    messages.success(request,"Your skill is deleted")
    return redirect("Home:skill_details_page",slug=slug)




def create_portfolio(request,slug):
    portfolio_data={}
    portfolio_data['user_info']=UserInfo.objects.get(slug=slug)
    name=UserInfo.objects.get(slug=slug)
    # print(name)
    portfolio_data['education']=Education.objects.filter(slug=name).all()
    portfolio_data['skills']=Skill.objects.filter(slug=name).all()
    portfolio_data['experience']=Experience.objects.filter(slug=name).all()
    portfolio_data['project']=Project.objects.filter(slug=name).all()

    print(portfolio_data)
    return render(request,"Portfolio.html",{'portfolio_data':portfolio_data})

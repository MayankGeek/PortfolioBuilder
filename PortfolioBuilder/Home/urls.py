from django.contrib import admin
from django.urls import path
from .import views


app_name="Home"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('get_details_form/',views.get_details_form,name='get_details_form'),
    path('details_page/<slug>/',views.details_page,name='details_page'),
    path('change_info/<slug>/',views.change_info,name='change_info'),
    path('add_skills_form/<slug>/',views.add_skills_form,name='add_skills_form'),
    path('add_education_form/<slug>/',views.add_education_form,name='add_education_form'),
    path('education_details_page/<slug>/',views.education_details_page,name='education_details_page'),
    path('skill_details_page/<slug>/',views.skill_details_page,name='skill_details_page'),
    path('add_education_form/',views.add_education_form,name='add_education_form'),
    path('education_details_page/',views.education_details_page,name='education_details_page'),
    path('add_expertise_form/',views.add_expertise_form,name='add_expertise_form'),
    path('expertise_details_page/',views.expertise_details_page,name='expertise_details_page'),
    path('add_experience_form/<slug>/',views.add_experience_form,name='add_experience_form'),
    path('experience_details_page/<slug>/',views.experience_details_page,name='experience_details_page'),
    path('add_project_form/<slug>/',views.add_project_form,name='add_project_form'),
    path('project_details_page/<slug>/',views.project_details_page,name='project_details_page'),
    path('user_portfolios/',views.user_portfolios,name='user_portfolios'),
]

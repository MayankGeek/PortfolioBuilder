from django import forms
from .models import UserInfo,Skill,Education,Experience,Project
class UserInfoForm(forms.ModelForm):

    linkedin_url = forms.URLField(required=False)  # Make the field optional
    class Meta:
        model=UserInfo
        fields=['name','mobile_no','email','about','profession','place','profile_picture','linkedin_url']

class AddSkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        # fields=['skill1','percent1','skill2','percent2','skill3','percent3','skill4','percent4','skill5','percent5',]
        fields=['skill','percent']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=['board_or_univ','course','cgpa_or_percent','cgpa']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        fields=['organisation_name','position','joining_date','ending_date','work_experience']

class ProjectForm(forms.ModelForm):
    project_link = forms.URLField(required=False)  # Make the field optional

    class Meta:
        model=Project
        fields=['project_name','project_desc','project_start_date','project_end_date','project_link']








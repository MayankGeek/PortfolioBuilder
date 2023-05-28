from django import forms
from .models import UserInfo,Skill,Education,Experience

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['name','mobile_no','email','about','profession','place','profile_picture']

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









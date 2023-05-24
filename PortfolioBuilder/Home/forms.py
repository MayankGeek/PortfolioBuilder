from django import forms
from .models import UserInfo,Skill

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['name','mobile_no','email','about','profession','place','profile_picture']

class AddSkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields=['skill1','percent1','skill2','percent2','skill3','percent3','skill4','percent4','skill5','percent5',]








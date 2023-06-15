from django.shortcuts import reverse
from django.db import models
from django.utils.text import slugify
from django.conf import settings
import itertools
import random
import string

class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="images")
    email = models.EmailField()
    about = models.TextField()
    mobile_no = models.DecimalField(max_digits=10, decimal_places=0)
    slug = models.SlugField(unique=True)
    profession = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    linkedin_url= models.URLField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.slug

    def _generate_slug(self):
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        value = self.name + res
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not UserInfo.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def get_slug(self):
        return self.slug

    def slug_save(self, *args, **kwargs):
        self._generate_slug()

        super().save(*args, **kwargs)

    def get_img_url(self, slug):
        return reverse('home:media', kwargs={'slug':slug})

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, blank=True, null=True)
    skill = models.CharField(max_length=50, null=True, blank=True)
    percent = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    def __str__(self):
        return self.slug.name

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, blank=True, null=True)
    board_or_univ = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    cgpa_or_percent = models.DecimalField(max_digits=4, decimal_places=2)
    cgpa = models.BooleanField(default=False)

    def __str__(self):
        return self.slug.name

class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, blank=True, null=True)
    organisation_name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    joining_date = models.DateField()
    ending_date = models.DateField( blank=True, null=True)
    work_experience = models.TextField()

    def __str__(self):
        return self.slug.name
    
class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, blank=True, null=True)
    project_name = models.CharField(max_length=50, null=True, blank=True)
    project_desc = models.TextField()
    project_start_date = models.DateField()
    project_end_date = models.DateField( blank=True, null=True)
    project_link = models.URLField(max_length=2084, null=True, blank=True)



    def __str__(self):
        return self.slug.name

# class SocialLinks(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
#     slug = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, blank=True, null=True)
#     linkedin_url= models.URLField(max_length=250,null=True, blank=True)
#     def __str__(self):
#         return self.slug.name
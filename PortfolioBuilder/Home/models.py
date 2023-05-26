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
    # skill2 = models.CharField(max_length=50, null=True, blank=True)
    # percent2 = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    # skill3 = models.CharField(max_length=50, null=True, blank=True)
    # percent3 = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    # skill4 = models.CharField(max_length=50, null=True, blank=True)
    # percent4 = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    # skill5 = models.CharField(max_length=50, null=True, blank=True)
    # percent5 = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    def __str__(self):
        return self.slug.name
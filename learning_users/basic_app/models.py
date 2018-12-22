from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    # additional classes
    portfolio_site= model.URLField(blank=True)
    profile_pic = model.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

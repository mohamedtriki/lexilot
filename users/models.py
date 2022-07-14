from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    plans=(("basic","basic"),("pro","pro"),("business","business"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    html=models.TextField(default="",blank=True)
    css=models.TextField(default="",blank=True)
    plan = models.CharField(max_length=200,choices=plans)
    domain_name = models.CharField(max_length=200,default="",blank=True)
    website_img = models.ImageField(blank=True )
    website_name = models.CharField(max_length=200,default="",blank=True)
    template_name = models.CharField(max_length=200,default="",blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class payment(models.Model):
        user = models.CharField(max_length=200,null=True,blank=True)
        amount=models.FloatField(help_text = "use . not ,",default=0,blank=True,null=True)
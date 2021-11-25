from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        subject = 'Welcome to The Buddy Clubhouse!'
        message = 'Thank you for joining us in making a difference in the lives of our canine friends.'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email]
            fail_silently=False,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance 
    user = profile.user

    if created is False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.user.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
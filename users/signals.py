from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        subject = render_to_string(
            'user/confirmation_emails/registration_success_subject.txt',
            {'user': user})
        body = render_to_string(
            'user/confirmation_emails/registration_sucess_body.txt',
            {'user': user, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created is False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)

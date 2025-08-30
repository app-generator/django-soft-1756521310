# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Beneficiare(models.Model):

    #__Beneficiare_FIELDS__
    idben = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    profession = models.TextField(max_length=255, null=True, blank=True)
    geo4_id = models.ForeignKey(LOCALISATION, on_delete=models.CASCADE)

    #__Beneficiare_FIELDS__END

    class Meta:
        verbose_name        = _("Beneficiare")
        verbose_name_plural = _("Beneficiare")


class Localisation(models.Model):

    #__Localisation_FIELDS__
    geo_type = models.IntegerField(null=True, blank=True)
    geo_fat_id = models.IntegerField(null=True, blank=True)

    #__Localisation_FIELDS__END

    class Meta:
        verbose_name        = _("Localisation")
        verbose_name_plural = _("Localisation")


class Member_Menage(models.Model):

    #__Member_Menage_FIELDS__
    id_menage = models.ForeignKey(BENEFICIARE, on_delete=models.CASCADE)
    id_member = models.CharField(max_length=255, null=True, blank=True)
    nom_mem = models.CharField(max_length=255, null=True, blank=True)
    prenom_mem = models.CharField(max_length=255, null=True, blank=True)

    #__Member_Menage_FIELDS__END

    class Meta:
        verbose_name        = _("Member_Menage")
        verbose_name_plural = _("Member_Menage")



#__MODELS__END

import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Developer(models.Model):
    appid = models.OneToOneField('Steamfacttable', models.DO_NOTHING, db_column='AppID', primary_key=True)  # Field name made lowercase. The composite primary key (AppID, Developers) found, that is not supported. The first column is selected.
    developers = models.CharField(db_column='Developers', max_length=600)  # Field name made lowercase.
    publishers = models.CharField(db_column='Publishers', max_length=600, blank=True, null=True)  # Field name made lowercase.
    categories = models.TextField(db_column='Categories', blank=True, null=True)  # Field name made lowercase.
    genres = models.TextField(db_column='Genres', blank=True, null=True)  # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True, null=True)  # Field name made lowercase.
    screenshots = models.TextField(db_column='Screenshots', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'developer'
        unique_together = (('appid', 'developers'),)


class Gameinfo(models.Model):
    appid = models.OneToOneField('Steamfacttable', models.DO_NOTHING, db_column='AppID', primary_key=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    about_the_game = models.TextField(db_column='About the game', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supported_languages = models.TextField(db_column='Supported Languages', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    audio_languages = models.TextField(db_column='Audio Languages', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    website_url = models.TextField(db_column='Website URL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    support_url = models.TextField(db_column='Support URL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    support_email = models.TextField(db_column='Support Email', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    windows = models.IntegerField(db_column='Windows', blank=True, null=True)  # Field name made lowercase.
    mac = models.IntegerField(db_column='Mac', blank=True, null=True)  # Field name made lowercase.
    linux = models.IntegerField(db_column='Linux', blank=True, null=True)  # Field name made lowercase.
    achievements = models.IntegerField(db_column='Achievements', blank=True, null=True)  # Field name made lowercase.
    recommendations = models.IntegerField(db_column='Recommendations', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    header_image = models.TextField(db_column='Header Image', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dlc_count = models.IntegerField(db_column='DLC Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'gameinfo'


class Playtime(models.Model):
    appid = models.OneToOneField('Steamfacttable', models.DO_NOTHING, db_column='AppID', primary_key=True)  # Field name made lowercase.
    average_playtime = models.IntegerField(db_column='Average Playtime', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_playtime_2_weeks = models.IntegerField(db_column='Average Playtime 2 Weeks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    median_playtime = models.IntegerField(db_column='Median Playtime', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    median_playtime_2_weeks = models.IntegerField(db_column='Median Playtime 2 Weeks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'playtime'


class Review(models.Model):
    appid = models.OneToOneField('Steamfacttable', models.DO_NOTHING, db_column='AppID', primary_key=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    metacritic_score = models.IntegerField(db_column='Metacritic Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metacritic_url = models.TextField(db_column='Metacritic URL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_score = models.IntegerField(db_column='User Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    positive = models.IntegerField(db_column='Positive', blank=True, null=True)  # Field name made lowercase.
    negative = models.IntegerField(db_column='Negative', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class Steamfacttable(models.Model):
    appid = models.IntegerField(db_column='AppID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    minimum_owners = models.IntegerField(db_column='Minimum owners', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maximum_owners = models.IntegerField(db_column='Maximum owners', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    peak_ccu = models.IntegerField(db_column='Peak CCU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    required_age = models.IntegerField(db_column='Required age', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'steamfacttable'
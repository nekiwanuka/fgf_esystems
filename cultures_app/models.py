from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clan(models.Model):
    clan_name = models.CharField(max_length=250, null=True, blank=True)
    clan_seat = models.CharField(max_length=250, null=True, blank=True)
    totem = models.CharField(max_length=250, null=True, blank=True)
    secondary_totem = models.CharField(max_length=250, null=True, blank=True)
    clan_history = models.TextField(null=True, blank=True)
    clan_leader_title = models.CharField(max_length=250, null=True, blank=True)
    clan_leader_name = models.CharField(max_length=250, null=True, blank=True)
    cultural_sites = models.TextField(null=True, blank=True)
    male_names = models.TextField(null=True, blank=True) #male_names_meaning = models.CharField(max_length=250)
    female_names = models.TextField(null=True, blank=True) #female_name_meaning = models.CharField(max_length=250) 
    reserved_male_names  = models.TextField(null=True, blank=True)
    reserved_female_names  = models.TextField(null=True, blank=True) #Meaning  = models.CharField(max_length=250) 
    taboos = models.CharField(max_length=250, null=True, blank=True)   
    lead_god = models.CharField(max_length=250, null=True, blank=True) #should we add a model for this?
    other_gods = models.CharField(max_length=250) #roles  = models.CharField(max_length=250) 
    
    """ image = models.ImageField(upload_to='culture_images', null=True, blank=True)
    video = models.FileField(upload_to='culture_videos', null=True, blank=True)
    audio = models.FileField(upload_to='culture_audio', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.TextField(null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True) """


class CulturalKingdom(models.Model):
    kingdom_name = models.CharField(primary_key=True, max_length=250) 
    title_of_leader = models.CharField(max_length=250, null=True, blank=True)
    current_king = models.CharField(max_length=250, null=True, blank=True)
    current_chief_name = models.CharField(max_length=250, null=True, blank=True)
    """ image = models.ImageField(upload_to='culture_images', null=True, blank=True)
    video = models.FileField(upload_to='culture_videos', null=True, blank=True)
    audio = models.FileField(upload_to='culture_audio', null=True, blank=True) """
    number_of_clans = models.IntegerField(default=1, null=True)
    clan_name = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True)
  
      

class Ethnicity(models.Model): 
    ethnicity_name = models.CharField(primary_key=True, max_length=250) 
    region_in_Uganda = models.CharField(max_length=250, null=True, blank=True) 
    language = models.CharField(max_length=250, null=True, blank=True)
    food = models.CharField(max_length=250, null=True, blank=True)
    staple_food = models.CharField(max_length=250, null=True, blank=True)
    cuisine = models.CharField(max_length=250, null=True, blank=True)
    cashcrop = models.CharField(max_length=250, null=True, blank=True)
    universal_worship = models.CharField(max_length=250, null=True, blank=True)
    denominations = models.CharField(max_length=250, null=True, blank=True)
    universal_rituals = models.CharField(max_length=250, null=True, blank=True)
    ceremonies = models.CharField(max_length=250, null=True, blank=True)
    kingdom = models.ForeignKey(CulturalKingdom, on_delete=models.SET_NULL, null=True)
    chiefdom = models.CharField(max_length=250, null=True, blank=True)
    
    """ image = models.ImageField(upload_to='culture_images', null=True, blank=True)
    video = models.FileField(upload_to='culture_videos', null=True, blank=True)
    audio = models.FileField(upload_to='culture_audio', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.TextField(null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True) """

    def __str__(self) -> str:
        return self.ethnicity_name
    
class EthnicGroup(models.Model):
    ethnic_group_name = models.CharField(max_length=250, null=True, blank=True)
    region_in_Uganda = models.CharField(max_length=250, null=True, blank=True)
    number_of_ethnicities = models.IntegerField(default=1, null=True, blank=True)
    number_of_languages = models.IntegerField(default=1, null=True)
    number_of_kingdoms = models.IntegerField(default=1, null=True)
    ethnicity_name = models.ForeignKey(Ethnicity, on_delete=models.SET_NULL, null=True)

    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='culture_images', null=True, blank=True)
    video = models.FileField(upload_to='culture_videos', null=True, blank=True)
    audio = models.FileField(upload_to='culture_audio', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.TextField(null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.ethnic_group
    
    class Meta:
        pass

    def total_entries(self):

        return Clan.objects.filter(clan_name=self.clan_name).count()




# Not needed
class CulturalIdentity(models.Model):
    ethnic_group = models.ForeignKey(EthnicGroup, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(null=True, blank=True)
    # contributor_name = models.CharField(max_length=250)  ---Repeated field
    # citation = models.CharField(max_length=250) ---Repeate field
    image = models.ImageField(upload_to='culture_images', null=True, blank=True)
    video = models.FileField(upload_to='culture_videos', null=True, blank=True)
    audio = models.FileField(upload_to='culture_audio', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.TextField(null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.ethnic_group
    
    class Meta:
        pass


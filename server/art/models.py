from django.db import models
from moonmask.collage import Collage
from api.models import User

# Create your models here.
#

class Artwork(models.Model):
    #using camel case for model fields because
    #solutions for dash vs underscore serialization in
    #ember.js are elusive at the moment
    title = models.TextField(max_length=50,
                             default='Untitled')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="artwork",
                              null=True,
                              blank=True)
    moonRelativeDate = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    moonDate = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    mainImageUrl = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    mainImageInstagramUrl = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    mainImageColor = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    maskPositiveSpaceUrl = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    maskPositiveSpaceInstagramUrl = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    maskPositiveSpaceColor = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    maskNegativeSpaceUrl = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    maskNegativeSpaceInstagramUrl = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    maskNegativeSpaceColor = models.TextField(max_length=1000,
                                          null=True,
                                          blank=True)
    negativeSpaceTransparency = models.TextField(max_length=3,
                                                   null=True,
                                                   blank=True)
    positiveSpaceTransparency = models.TextField(max_length=3,
                                                   null=True,
                                                   blank=True)
    dimensionality = models.TextField(max_length=3,
                                      null=True,
                                      blank=True)

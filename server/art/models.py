from django.db import models
from moonmask.collage import Collage
from api.models import User

#processing and saving images files
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

#for signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from functools import wraps

# Create your models here.

class Artwork(models.Model):
    #using camel case for model fields because
    #solutions for dash vs underscore serialization in
    #ember.js are elusive at the moment
    title = models.TextField(max_length=50,
                             default='Untitled')
    #TODO reinstate author after you figure out user auth for ember
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
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


#very helpful thing about decorators and skipping signals
#https://stackoverflow.com/a/27161229/5650506
def skip_signal():
    def _skip_signal(signal_func):
        @wraps(signal_func)
        def _decorator(sender, instance, **kwargs):
            if hasattr(instance, 'skip_signal'):
                return None
            return signal_func(sender, instance, **kwargs)
        return _decorator
    return _skip_signal

# method for updating
@receiver(post_save, sender=Artwork, dispatch_uid="make_image")
@skip_signal()
def make_image(sender, instance, **kwargs):
    print("starting make image")
    c = Collage()
    c.set_mask()
    c.set_main_image("pink", color="pink")
    c.set_mask_positive_space("yellow", color="yellow")
    c.set_mask_negative_space("black", color="black")
    c.create_collage()
    im = c.get_created_collage()
    file_name=instance.title + ".jpg"
    buffer = BytesIO()
    im.save(fp=buffer, format='PNG')
    pillow_image = ContentFile(buffer.getvalue())
    print("saving...")
    instance.skip_signal = True
    instance.image.save(file_name, InMemoryUploadedFile(
                pillow_image,
                None,
                file_name,
                'image/jpeg',
                pillow_image.tell,
                None
    ))
    print("finished with maek iamge")

from django.db import models

from django.utils.text import slugify
from django.urls import reverse,reverse_lazy
from django.conf import settings


# Create your models here.

class Image(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="images_created")

    title = models.CharField(max_length=450)

    slug = models.SlugField(max_length=450,blank=True)

    image = models.ImageField(upload_to="bookmarks/%y/%m/%d")

    description = models.TextField(blank=True)

    url = models.URLField()

    created = models.DateTimeField(auto_now_add=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="images_liked",blank=True)

    def __str__ (self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Image,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse ("images:image_detail",args=[self.id,self.slug])

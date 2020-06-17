from django import forms

from .models import Image

from urllib import request

from django.core.files.base import ContentFile

from django.utils.text import slugify


class ImageCreationForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ["title","url","description"]
        widgets = {
            'url':forms.HiddenInput,
        }

    def clean_url (self):

        url = self.cleaned_data['url']

        valid_extensions = ["jpg","jpeg","png"]

        extension = url.rsplit(".",1)[1].lower()

        if extension not in valid_extensions:
            raise forms.ValidationEror("The given URL does not match any valid image extensions\nThe valid extensions ar jpg jpeg png")

        return url

    def save(self,force_insert=False,force_update=False,commit=True):

        image = super(ImageCreationForm,self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = "{}.{}".format(slugify(image.title),image_url.rsplit(".",1)[1].lower())

        #download image from the URL

        response = request.urlopen(image_url) # we get the the address of the image
        image.image.save(image_name,ContentFile(response.read()),save=False)

        if commit:
            image.save()
        return image

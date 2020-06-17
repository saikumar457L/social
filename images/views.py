from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from .forms import ImageCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image

from django import forms

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from common.decorators import ajax_required

from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

@login_required
def image_create(request):

    if request.method == "POST":
        image_form = ImageCreationForm(data=request.POST)

        if image_form.is_valid():
            cd = image_form.cleaned_data
            new_image = image_form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request,"Image upload success")
            return redirect(new_image.get_absolute_url())

        else:

            messages.error(request,"Image upload failed")
            raise forms.ValidationEror("Something went wrong.")

    else:
        image_form = ImageCreationForm(data=request.GET)

    return render(request,"images/create_image.html",{"image_form":image_form,"section":"images"})


def image_detail(request,id,slug):
    image = get_object_or_404(Image,id=id,slug=slug)

    return render(request,"images/image_detail.html",{"section":"images","image":image})

@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images,5)
    page = request.GET.get('page')

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse("")

        images = paginator.page(paginator.num_pages)

    if request.is_ajax():
        return render(request,"images/list_ajax.html",{"section":"images","images":images})

    return render(request,"images/list.html",{"section":"images","images":images})

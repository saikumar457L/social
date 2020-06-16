from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.models import User

from .forms import UserRegistrationForm

from django.http import JsonResponse

from .models import Profile
from .forms import UserEditForm,ProfileEditForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.urls import reverse,reverse_lazy

# Create your views here.

class AccountsSiteHome(TemplateView):
    template_name = "site/home.html"


def user_register(request):

    if request.method == "POST":
        user_form = UserRegistrationForm(data=request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # setting the user wanted password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user) # Custom user register user form extension

            return render (request,'accounts/user_register_done.html',{"new_user":new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request,"accounts/user_register.html",{"user_form":user_form})

def validate_user_register(request):

    username = request.GET.get('username',None)
    email = request.GET.get('email',None)

    data = {
        'is_taken':User.objects.filter(username__iexact = username).exists(),
        'mail_taken': User.objects.filter(email__iexact = email).exists(),
    }

    if data['is_taken']:
        data['error_message'] = "The requested username is already taken"
    elif data['mail_taken']:
        data['mail_error'] = "The given mail is already taken. Please try another one."

    return JsonResponse(data)



class AccountDetails(LoginRequiredMixin,TemplateView):
    template_name = "accounts/account_details.html"

@login_required
def update_profile(request):
    if request.method == "POST":

        user_form = UserEditForm(instance=request.user,data=request.POST)

        profile_form = ProfileEditForm(instance = request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profile updated successfully.")

            return render(request,"accounts/account_details.html")
        else:
            messages.error(request,"Profile update Fail. Please try again.")

    else:
        try:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
            return render (request,"accounts/update_profile.html",{"user_form":user_form,"profile_form":profile_form})

        except :
            return render (request,"accounts/update_profile.html",{"user_form":user_form})

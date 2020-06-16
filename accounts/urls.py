from django.urls import path

from django.contrib.auth import views as auth_views


from .views import AccountsSiteHome,user_register,validate_user_register
from .views import update_profile,AccountDetails


urlpatterns = [
    path("login/",auth_views.LoginView.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("password_change/",auth_views.PasswordChangeView.as_view(),name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path("password_reset/",auth_views.PasswordResetView.as_view(),name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password_reset/<uidb64>/<token>/confirm/",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("password_reset/complete/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("",AccountsSiteHome.as_view(),name="home"),
    path("create-account/",user_register,name="create_account"),
    path("validate-user-form/",validate_user_register,name="validate_user_register"),
    path("account-details/",AccountDetails.as_view(),name="account_details"),
    path("update-profile/",update_profile,name="update_profile"),

]

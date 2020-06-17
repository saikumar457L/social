from django.urls import path

from .views import image_create,image_detail,image_like
from .views import image_list


app_name = "images"

urlpatterns = [
    path("create/",image_create,name="create"),
    path("image-detail/<int:id>/<slug:slug>/",image_detail,name="image_detail"),
    path("like/",image_like,name="like"),
    path("bookmarked-images/",image_list,name="list"),
]

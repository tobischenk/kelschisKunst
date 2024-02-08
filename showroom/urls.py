from django.urls import path

from . import views

urlpatterns = [
    path("showroom/", views.ShowroomIndexView.as_view(), name="index"),
]

from django.urls import path, include
from lost import views
urlpatterns = [
    path("", views.create, name = "create"),
    path("retrieve/", views.retrieve, name = "retrieve"),
    path('location/',views.location, name= "location"),
    path("delete/<slug:id>", views.delete, name = "delete"),
    path("update/<slug:id>", views.update, name = "update"),
    path("updaterecord/<slug:id>", views.updaterecord, name = "updaterecord"),
    path("deleteloc/<slug:loc_id>", views.deleteloc, name = "deleteloc"),
#

]

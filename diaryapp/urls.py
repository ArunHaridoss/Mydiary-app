from django.urls import path
from . import views
from .views import customLoginView
from django.contrib.auth.views import LogoutView

urlpatterns =[ 
    path("login/",customLoginView.as_view(),name="login"),
    path("",views.home,name="home"),
    path("notes/",views.notes,name="notes"),
    path("create-notes/",views.createNotes, name="create-notes"),
    path("update-notes/<str:pk>",views.updateNotes, name="update-notes"),
    path('delete-notes/<str:pk>',views.deleteNotes, name="delete-notes"),
    path("logout/",LogoutView.as_view(next_page="home"),name="logout")
]
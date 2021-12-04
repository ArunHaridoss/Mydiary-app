from django.urls import path
from . import views

urlpatterns =[ 
    path("",views.home,name="home"),
    path("notes/",views.notes,name="notes"),
    path("create-notes/",views.createNotes, name="create-notes"),
    path("update-notes/<str:pk>",views.updateNotes, name="update-notes"),
    path('delete-notes/<str:pk>',views.deleteNotes, name="delete-notes"),
    path('register/',views.Register, name="register")
]
# glossary/urls.py
from django.urls import path
from glossary import views

urlpatterns = [
    #
    # create views
    #
    path("term/create/", views.create_term, name="create_term"),
    #
    # update views
    #
    path("term/update/<int:term_id>", views.update_term, name="update_term"),
    #
    # update views
    #
    path("term/delete/<int:term_id>/", views.delete_term, name="delete_term"),
]

# notes/urls.py
from django.urls import path
from notes import views

urlpatterns = [
    #
    # detail views
    #
    path(
        "certification/<int:id>/<slug:slug>/",
        views.certification_detail,
        name="certification_detail",
    ),
    path("domain/<int:id>/<slug:slug>/", views.domain_detail, name="domain_detail"),
    path("entry/<int:id>/<slug:slug>/", views.entry_detail, name="entry_detail"),
    #
    # create views
    #
    path(
        "certification/create/", views.create_certification, name="create_certification"
    ),
    path(
        "domain/create/<int:certification_id>",
        views.create_domain,
        name="create_domain",
    ),
    path("entry/create/<int:domain_id>", views.create_entry, name="create_entry"),
    #
    # update views
    #
    path(
        "certification/update/<int:certification_id>",
        views.update_certification,
        name="update_certification",
    ),
    path("domain/update/<int:domain_id>", views.update_domain, name="update_domain"),
    path("entry/update/<int:entry_id>", views.update_entry, name="update_entry"),
    #
    # update views
    #
    path(
        "certification/delete/<int:certification_id>/",
        views.delete_certification,
        name="delete_certification",
    ),
    path("domain/delete/<int:domain_id>/", views.delete_domain, name="delete_domain"),
    path("entry/delete/<int:entry_id>/", views.delete_entry, name="delete_entry"),
    #
    # additional urls
    #
    path("entry/share/<int:entry_id>/", views.entry_share, name="entry_share"),
]

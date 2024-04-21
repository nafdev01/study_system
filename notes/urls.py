# notes/urls.py
from django.urls import path
from notes import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    #
    # detail views
    #
    path(
        "course/<int:id>/<slug:slug>/",
        views.course_detail,
        name="course_detail",
    ),
    path("domain/<int:id>/<slug:slug>/", views.domain_detail, name="domain_detail"),
    path("entry/<int:id>/<slug:slug>/", views.entry_detail, name="entry_detail"),
    #
    # create views
    #
    path("course/create/", views.create_course, name="create_course"),
    path(
        "domain/create/<int:course_id>",
        views.create_domain,
        name="create_domain",
    ),
    path("entry/create/<int:domain_id>", views.create_entry, name="create_entry"),
    #
    # update views
    #
    path(
        "course/update/<int:course_id>",
        views.update_course,
        name="update_course",
    ),
    path("domain/update/<int:domain_id>", views.update_domain, name="update_domain"),
    path("entry/update/<int:entry_id>", views.update_entry, name="update_entry"),
    #
    # update views
    #
    path(
        "course/delete/<int:course_id>/",
        views.delete_course,
        name="delete_course",
    ),
    path("domain/delete/<int:domain_id>/", views.delete_domain, name="delete_domain"),
    path("entry/delete/<int:entry_id>/", views.delete_entry, name="delete_entry"),
    #
    # additional urls
    #
    path("entry/share/<int:entry_id>/", views.entry_share, name="entry_share"),
]

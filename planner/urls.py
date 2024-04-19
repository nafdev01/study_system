from django.urls import path
from planner import views


urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
]
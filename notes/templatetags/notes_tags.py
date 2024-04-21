from django import template
from django.utils.safestring import mark_safe
import markdown
from notes.models import Course

register = template.Library()


@register.inclusion_tag("includes/dash-courses.html")
def dash_courses(student):
    courses = Course.objects.filter(student_id=student.id)
    return {"courses": courses}


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag("includes/nav-courses.html")
def nav_courses(student):
    courses = Course.objects.filter(student_id=student.id)
    return {"courses": courses}

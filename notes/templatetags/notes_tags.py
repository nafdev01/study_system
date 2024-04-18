from django import template
from django.utils.safestring import mark_safe
import markdown
from notes.models import Certification

register = template.Library()


@register.inclusion_tag("includes/dash-certs.html")
def dash_certs(student):
    certifications = Certification.objects.filter(student_id=student.id)
    return {"certifications": certifications}


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag("includes/nav-certs.html")
def nav_certs(student):
    certifications = Certification.objects.filter(student_id=student.id)
    return {"certifications": certifications}

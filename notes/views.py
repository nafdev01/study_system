from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from notes.models import Domain, Certification, Entry
from notes.forms import CertificationForm, DomainForm, EntryForm


@login_required
def certification_detail(request, id, slug):
    student = request.user
    certification = get_object_or_404(
        Certification, id=id, slug=slug, student_id=student.id
    )
    domains = certification.domains.filter(
        certification__student_id=student.id, certification_id=certification.id
    )

    template_path = "notes/certification_detail.html"
    context = {
        "student": student,
        "certification": certification,
        "domains": domains,
        "section": certification.abbreviation,
    }
    return render(request, template_path, context)


@login_required
def create_certification(request):
    student = request.user
    if request.method != "POST":
        form = CertificationForm()
    else:
        form = CertificationForm(data=request.POST)
        if form.is_valid():
            new_certification = form.save(commit=False)
            new_certification.student = student
            new_certification.save()
            return redirect(new_certification)

    template_path = "notes/certification_create_form.html"
    context = {"form": form}
    return render(request, template_path, context)


@login_required
def update_certification(request, certification_id):
    certification = Certification.objects.get(id=certification_id)
    if request.method != "POST":
        form = CertificationForm(instance=certification)
    else:
        form = CertificationForm(instance=certification, data=request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.save()
            return redirect(certification)

    template_path = "notes/certification_update_form.html"
    context = {"form": form, "certification": certification}
    return render(request, template_path, context)


@login_required
def delete_certification(request, certification_id):
    student = request.user
    certification = Certification.objects.get(
        id=certification_id, student_id=student.id
    )
    certification_name = certification.name

    certification.delete()
    messages.success(
        request,
        f"The certification {certification_name} has been deleted successfully.",
    )

    return redirect("dashboard")


"""
domain views
"""


@login_required
def domain_detail(request, id, slug):
    student = request.user
    domain = get_object_or_404(
        Domain, id=id, slug=slug, certification__student_id=student.id
    )

    template_path = "notes/domain_detail.html"
    context = {
        "student": student,
        "domain": domain,
    }
    return render(request, template_path, context)


@login_required
def create_domain(request, certification_id):
    student = request.user
    certification = get_object_or_404(
        Certification, id=certification_id, student_id=student.id
    )
    if request.method != "POST":
        form = DomainForm()
    else:
        form = DomainForm(data=request.POST)
        if form.is_valid():
            try:
                new_domain = form.save(commit=False)
                new_domain.certification = certification
                new_domain.save()
                return redirect(new_domain)
            except IntegrityError as e:
                if "duplicate key value violates unique constraint" in str(e):
                    messages.error(
                        request,
                        f'A domain with that number already exists in this certification "{certification.abbreviation}".',
                    )
                else:
                    messages.error(request, "There was an error creating the domain.")

    template_path = "notes/domain_create_form.html"
    context = {"form": form}
    return render(request, template_path, context)


@login_required
def update_domain(request, domain_id):
    domain = Domain.objects.get(id=domain_id)
    if request.method != "POST":
        form = DomainForm(instance=domain)
    else:
        form = DomainForm(instance=domain, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(domain)

    template_path = "notes/domain_update_form.html"
    context = {"form": form, "domain": domain}
    return render(request, template_path, context)


@login_required
def delete_domain(request, domain_id):
    student = request.user
    domain = Domain.objects.get(id=domain_id, certification__student_id=student.id)
    domain_name = domain.name
    certification = domain.certification

    domain.delete()
    messages.success(
        request, f"The domain {domain_name} has been deleted successfully."
    )

    return redirect(certification)


"""
entry views
"""


@login_required
def entry_detail(request, id, slug):
    student = request.user
    entry = get_object_or_404(
        Entry, id=id, slug=slug, domain__certification__student_id=student.id
    )

    template_path = "notes/entry_detail.html"
    context = {
        "student": student,
        "entry": entry,
    }
    return render(request, template_path, context)


@login_required
def create_entry(request, domain_id):
    student = request.user
    domain = get_object_or_404(
        Domain, id=domain_id, certification__student_id=student.id
    )
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            try:
                new_entry = form.save(commit=False)
                new_entry.domain = domain
                new_entry.save()
                return redirect(new_entry)

            except IntegrityError as e:
                if "duplicate key value violates unique constraint" in str(e):
                    messages.error(
                        request,
                        f'An entry with that title already exists in domain "{domain}".',
                    )
                else:
                    messages.error(request, "There was an error creating the entry.")

    template_path = "notes/entry_create_form.html"
    context = {"form": form}
    return render(request, template_path, context)


@login_required
def update_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(entry)

    template_path = "notes/entry_update_form.html"
    context = {"form": form, "entry": entry}
    return render(request, template_path, context)


@login_required
def delete_entry(request, entry_id):
    student = request.user
    entry = Entry.objects.get(
        id=entry_id, domain__certification__student_id=student.id
    )
    entry_name = entry.name
    domain = entry.domain

    entry.delete()
    messages.success(request, f"The entry {entry_name} has been deleted successfully.")

    return redirect(domain)


"""
Additional views
"""


# send entry by email
def entry_share(request, entry_id):
    student = request.user
    entry = get_object_or_404(
        Entry, id=entry_id, domain__certification__student_id=student.id
    )
    entry_url = request.build_absolute_uri(entry.get_absolute_url())
    subject = f"{student.get_full_name()} has sent you notes on {entry.domain}"
    sender = settings.EMAIL_HOST_USER
    recipient = request.GET.get("recipient")
    message = get_template("notes/includes/entry_email_template.html").render(
        {"entry": entry, "entry_url": entry_url}
    )
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=sender,
        to=[recipient],
        reply_to=[sender],
    )
    mail.content_subtype = "html"
    if mail.send():
        messages.success(
            request, f"The entry '{entry}'was successfully shared with '{recipient}'"
        )
    else:
        messages.error(
            request, f"The entry '{entry}' could not be shared with '{recipient}'"
        )

    return redirect(entry.domain.domain)

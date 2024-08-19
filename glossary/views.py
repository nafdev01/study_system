# glossary/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from notes.models import Course
from glossary.models import Term
from glossary.forms import TermForm, TermInlineForm


"""
create views
"""

@login_required
def term_list(request):
    student = request.user
    terms = Term.objects.filter(course__student=student)

    template_path = "glossary/term_list.html"
    context = {"terms": terms}
    return render(request, template_path, context)


@login_required
def create_term(request):
    student = request.user
    if request.method != "POST":
        form = TermForm(student=student)
    else:
        form = TermForm(student=student, data=request.POST)
        if form.is_valid():
            try:
                new_term = form.save(commit=False)
                new_term.save()
                return redirect(new_term)
            except IntegrityError as e:
                if "duplicate key value violates unique constraint" in str(e):
                    messages.error(request, f"A term with that title already exists")
                else:
                    messages.error(request, "There was an error creating the term.")

    template_path = "glossary/term_create_form.html"
    context = {"form": form}
    return render(request, template_path, context)


"""
update views
"""


@login_required
def update_term(request, term_id):
    student = request.user
    term = get_object_or_404(Term, id=term_id, course__student_id=student.id)
    course = term.course
    if request.method != "POST":
        form = TermForm(student=student, instance=term)
    else:
        form = TermForm(student=student, instance=term, data=request.POST)

        if form.is_valid():
            try:
                updated_term = form.save(commit=False)
                updated_term.save()
                messages.success(
                    request,
                    f"Successfully created term '{updated_term}' in {course.abbreviation}",
                )
                return redirect(updated_term)
            except IntegrityError as e:
                if "duplicate key value violates unique constraint" in str(e):
                    messages.error(request, f"A term with that title already exists")
                    return redirect(updated_term)
                else:
                    messages.error(request, "There was an error creating the term.")
                    return redirect(updated_term)

    template_path = "glossary/term_update_form.html"
    context = {"form": form, "term": term}
    return render(request, template_path, context)


"""
delete views
"""


@login_required
def delete_term(request, term_id):
    student = request.user
    term = Term.objects.get(id=term_id, course__student_id=student.id)
    term_name = term.name

    term.delete()
    messages.success(request, f"The term {term_name} has been deleted successfully.")

    return redirect("term_list")

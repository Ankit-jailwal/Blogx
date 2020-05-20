from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blogx.models import blogpost


def home_page(request):
    qs=blogpost.objects.all()[:5]
    context = {"title": "Welcome to Blogx","blog_list":qs}
    return render(request, "home.html", context)


def contact_page(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form= ContactForm()
    context={
        "title":"Contact Us",
        "form":form
    }
    return render(request, "form.html",  context)


def about_page(request):
    return render(request, "about.html", {"title": "ABOUT US"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "about.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Home Page"
    context={"title":my_title}
    if request.user.is_authenticated:
        context={"title":my_title,"my_list":[1,2,3,4,5]}
    return render(request,"home.html",context)

def contact_page(request):
    return render(request, "contact.html", {"title": "CONTACT US"})

def about_page(request):
    return render(request, "about.html", {"title": "ABOUT US"})

def example_page(request):
    context ={"title":"Example"}
    template_name="about.html"
    template_obj=get_template(template_name)
    return HttpResponse(template_obj.render(context))
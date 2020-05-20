from django.shortcuts import render

from .models import blogpost



def blog_post_detail_page(request):
    obj = blogpost.objects.get(id=2)
    template_name="blog_post_detail.html"
    context={"object":obj}
    return render(request,template_name,context)
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import (
    BlogPostForm,
    BlogPostModelForm,
)
from .models import blogpost


# def blog_post_detail_page(request, slug):
# queryset = blogpost.objects.filter(slug=slug)
# if queryset.count() == 0:
#   raise Http404
# obj = queryset.first()
# obj = get_object_or_404(blogpost, slug=slug)
# template_name = "blog_post_detail.html"
# context = {"object": obj}
# return render(request, template_name, context)


def blog_post_list_view(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        print(forms.cleaned_data)
    qs = blogpost.objects.all().published()
    if request.user.is_authenticated:
        my_qs=blogpost.objects.filter(user=request.user)
        qs= (qs | my_qs).distinct()
    template_name = "blog_post_list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)

@staff_member_required
# @login_required(login_url='/login')
def blog_post_create_view(request):
    #if not request.user.is_authenticated:
     #   template_name='not_a_user.html'

      #  return render(request, template_name,{})
    form = BlogPostModelForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # obj = blogpost.objects.create(**form.cleaned_data)
        form = BlogPostModelForm()
    template_name = "form.html"
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):

    obj = get_object_or_404(blogpost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(blogpost, slug=slug)
    form = BlogPostModelForm(request.POST or None , instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form':form,"title":f"Update {obj.title}"}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(blogpost, slug=slug)
    template_name = "blog_post_delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)

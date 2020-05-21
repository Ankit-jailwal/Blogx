from django.shortcuts import render
from .models import SearchQuery
from blogx.models import blogpost
# Create your views here.
def search_view(request):
    query=request.GET.get('q', None)
    user=None
    if request.user.is_authenticated:
        user=request.user
    context = {"query": query}
    if query is not None:
      SearchQuery.objects.create(user=user,query=query)
      blog_list=blogpost.objects.search(query=query)
      context['blog_list'] = blog_list
    return render(request,'searches/view.html',context)
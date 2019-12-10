from django.shortcuts import render, redirect
from .models import Blog
from . import forms


def modelformhome(request):
    if (request.method == 'POST'):
        form = forms.CreateBlog(request.POST)
        if(form.is_valid):
            form.save(commit=True)
            return redirect('modelformhome')
    else:
        form = forms.CreateBlog()

    blog_recs = []
    for record in Blog.objects.all():
        blog_recs.append({
            'title': record.title,
            'content': record.content
        })
    return render(request, 'v_modelforms/home.html', {'form': form, 'recs':blog_recs})

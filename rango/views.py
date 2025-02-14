from django.shortcuts import render, get_object_or_404
from rango.models import Category

def category_detail(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    pages = category.page_set.all()

    context_dict = {
        'category': category,
        'pages': pages,
    }

    return render(request, 'rango/category_detail.html', context=context_dict)

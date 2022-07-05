from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Author


def authors_list(request):

    q = request.GET.get('q')
    if q:
        authors = Author.objects.filter(Q(name__istartswith=q) | Q(last_name__istartswith=q))
    else:
        authors = Author.objects.all()

    p = Paginator(authors, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    return render(
        request,
        'authors/list.html',
        {'page_obj': page_obj}
    )


def author_details(request, pk):
    author = Author.objects.get(pk=pk)
    return render(
        request,
        'authors/details.html',
        {'author': author}
    )


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailsView(DetailView):
    model = Author
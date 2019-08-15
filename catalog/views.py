from django.http import Http404
from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, BookInstance


def index(request):
    # Hitung data dari object
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Buku tersedia (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' selalu terdefinisi sebagai default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['contoh'] = Book.objects.filter(title__icontains="Per").count()
        return context

    def get_queryset(self):
        return Book.objects.all()[:5]


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):

        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context

    def get_queryset(self):
        return Author.objects.all()[:5]


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):

        try:
            author = Author.objects.get(pk=primary_key)

        except Author.DoesNotExist:
            raise Http404('Author does not exist')

        return render(request, 'catalog/author_detail.html', context={'author': author})

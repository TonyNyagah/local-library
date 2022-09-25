from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # All books
    # all_books = Book.objects.all().order_by("title")

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = "a")
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The "all()" is implied by default.
    num_authors = Author.objects.count()

    # Available genres
    num_genres = Genre.objects.count()

    context = {
        # "all_books": all_books,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
    }

    # render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = (
        "book_list"  # your own name for the list as a template variable
    )
    # queryset = Book.objects.filter(title__icontains="war")[:5] # Get 5 books containing the title war
    template_name = "books/book_list.html"
    paginate_by = 5


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author

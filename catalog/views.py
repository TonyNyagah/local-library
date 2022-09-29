import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import RenewBookModelForm
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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        # "all_books": all_books,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
        "num_visits": num_visits,
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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""

    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by("due_back")
        )


class AllLoanedBooksByUserListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan."""

    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_librarian.html"
    paginate_by = 10
    permission_required = "catalog.can_mark_returned"

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact="o").order_by("due_back")


@login_required
@permission_required("catalog.can_mark_returned", raise_exception=True)
def renew_book_librarian(request, pk: int):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request the process the Form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding)
        form = RenewBookModelForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data["due_back"]
            book_instance.save()

            # redirect to a new URL
            return HttpResponseRedirect(reverse("all-borrowed-books"))
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = RenewBookModelForm(initial={"due_back": proposed_renewal_date})

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookModelForm(initial={"due_back": proposed_renewal_date})

        context = {"form": form, "book_instance": book_instance}

        return render(request, "catalog/book_renew_librarian.html", context)


class AuthorCreate(CreateView):
    model = Author
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]


class AuthorUpdate(UpdateView):
    model = Author
    fields = (
        "__all__"  # Not recommended (potential security issue if more fields are added)
    )


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy("authors")

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from project.forms import BookForm
from project.models import Book
from django.http import HttpResponse, HttpResponseRedirect



# class Home(generic.CreateView):
def home(request):
    return render(request, 'base.html')

class BookListView(generic.ListView):
    """ Renders a list of all projects. """
    model = Book

    def get(self, request):
        """ GET a list of projects. """
        books = self.get_queryset().all()
        return render(request, 'list.html', {
          'books': books
        })
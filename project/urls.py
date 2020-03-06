
from django.urls import path, include
from project.views import home, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

app_name = 'project'

urlpatterns = [
    path('', home, name='home_page'),
    path('list_of_books/', BookListView.as_view(), name='book-list-project'),
    path('new_book/', BookCreateView.as_view(), name='book-create-project'),
    path('<str:slug>/', BookDetailView.as_view(), name='book-details-project'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='book-update-project'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete-project'),
]
from django.urls import path

from relations.views import authors_list, author_details, AuthorListView, AuthorDetailsView

app_name = "publications"

urlpatterns = [
    path('authors/', authors_list, name='authors_list'),
    path('class/authors/', AuthorListView.as_view(), name='class_authors_list'),
    path('authors/<pk>/', author_details, name='author_details'),
    path('class/authors/<pk>/', AuthorDetailsView.as_view(), name='class_authors_list'),

]
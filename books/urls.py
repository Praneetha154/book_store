from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-book/',views.add_book,name='add'),
    path('book/<int:id>/', views.book_details, name='book_details'),
    path('edit/<int:id>/', views.edit_book, name='edit'),
    path('delete/<int:id>/', views.delete_book, name='delete'),
     path('about/',views.about,name='about'),
]
Simple Bookstore Application

  This is a simple Django-based bookstore application that allows users to manage a collection of books. Users can add, view, edit, and delete book entries. The application also includes optional search and 
  filter functionalities.

Features

     CRUD Operations:

        Create: Add new books to the collection.

        Read: View all books on the homepage.

       Update: Edit details of existing books.

       Delete: Remove books from the collection.

    Search Functionality: Search for books by title or author.

Requirements

    Python 

    Django

Installation

      Create a virtual environment:
   
          python -m venv myenv

      Activate the environment:
   
         `myenv\Scripts\activate`
       
      Install django:
   
          pip install django
        
      Run migrations:
   
         python manage.py migrate

     Create a superuser (optional, for admin access):
   
         python manage.py createsuperuser
       
     Run the development server:
   
         python manage.py runserver
       
     Access the application:
   
        Open your browser and go to http://127.0.0.1:8000/.


Screenshots

     Home Page

          ![Screenshot (4)](https://github.com/user-attachments/assets/1f992ed6-a579-4fec-b3b8-c43004f84380)


Usage

    Homepage: Displays all books with their title, author, and price.

    Add Book: Navigate to /add/ to add a new book.

    Edit Book: Click on the "Edit" button next to a book to edit its details.

    Delete Book: Click on the "Delete" button next to a book to remove it from the collection.

    View Details: Click on the "View Details" button to view all the details of the book.

    Search: Use the search bar to find books by title or author.

  

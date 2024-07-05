from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.


""" Read """
def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

"""
1. Index Function
This function is performing Read Operation. In this function, we simply retrieve all the objects in the book table. Those objects are then passed to the corresponding template.

We are using Querysets here for that purpose. As discussed in previous articles: Querysets is used to retrieve data from Tables. There are all kinds of filters and usage of Querysets and here we are using:

Book.objects.all()

It is clear from the query that it is passing a set of all objects in Book Table.
"""


######################################################################################################################################


""" CREATE Function """
def upload(request):
    upload_form = BookCreate()
    if request.method == 'POST':
        upload_form = BookCreate(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return redirect('index')  # Redirect to index after successful upload
        else:
            return HttpResponse("""Your form is incorrect, reload on <a href="{{ url : 'index' }}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form': upload_form})


"""
2. Upload Function

This function is CREATE operation of CRUD. It is simply taking form data from the user and saving it in a database. Since we made a model form for that, we don’t need to validate data again. We can directly save the form info in the database.

We first create the form object. Then we check whether the form is submitting data or user is visiting for the first time.

If the form request method is POST, it means the form is being submitted. You can see, it is also checked whether the form also has an image file or not. The request.FILES is a dictionary-like object containing the FILES and other information.

Then we check whether the data entered by the user is correct or not. This is done by form_object.is_clean() method. This will return True or False whether the form_object holds valid data or not.

If the answer is True, we save the form data received in the database. form_object.save() accomplishes this and since it’s a model form, we can use it directly.

If we receive a GET request then we return an empty form. That’s how we can create an object in the database.
"""


######################################################################################################################################


""" Update Function """
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form': book_form})

"""
3. Update_book Function

The update_book Function is a bit similar to the Update Function. It does more than that though. The update_book function takes in two parameters from the request. The request itself and id number. The id number is used to identify the object which is to be edited.

You can pass it in as a URL or as a cookie. The session method is the most secure but we don’t need to use it here. So, the update_book function will check whether the book_id is valid or not.

If the object exists it will return the form filled with the object’s information in it. The user can change the form again. In this case, there will be no creation of new book but the editing of the existing book object.
"""


######################################################################################################################################


""" Delete Function  """
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')


"""
4. Delete Function

Delete Function is the last function of the CRUD application. We are again using the same object method as with Update book function. We are passing the request and book_id to delete the book.

This is a simpler interpretation of update_book function.

The queryset book.objects.get(id = book_id) will check for the books having an id equal to book_id. Since book_id is a primary key, we will have only one object returned. We can delete that object easily by just executing:

Book.delete() method. This will delete the book from the database.

So, these were the view functions. Now, we are ready to make the templates and complete our app.
"""

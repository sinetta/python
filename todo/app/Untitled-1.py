<tr><th><label for="id_task">Task:</label></th><td><input type="text" name="task" value="dsgf" maxlength="255" required id="id_task"></td></tr>
<tr><th><label for="id_task">Task:</label></th><td><input type="text" name="task" value="sinetta raj" maxlength="255" required id="id_task"></td></tr>

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from books.models import Book,Author
from books.forms import BookForm, SearchForm
from users.models import User

def search_book(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form = SearchForm(request.POST)
            stitle = form.cleaned_data['title']
            sauthor = form.cleaned_data['author']
            scategory = form.cleaned_data['category']
    else:
        form = SearchForm()
    return render_to_response("books/create.html", {
        "form": form,
    }, context_instance=RequestContext(request))

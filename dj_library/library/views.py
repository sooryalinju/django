from http.client import HTTPResponse
from multiprocessing import context
from unittest import result
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Books, Members, Transactions
from .forms import BooksForm, MembersForm, TransactionsForm

# Create your views here.
# def registerPage(request):
#     form = CreateUserForm
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account created successfully for '+ user)
#             return redirect('/login/')
#     context={'form' : form}
#     return render(request, 'register.html', context )

# def loginPage(request):
#     context={}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('')
#         else:
#             messages.info(request, 'Username or Password is incorrect')
#             return render(request, 'login.html', context)
#     return render(request, 'index.html', context )

# def logoutUser(request):
#     return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def books(request):
    books_list = Books.objects.all()
    pages = pagination(request, books_list, 20)
    dict_books={
        'books': pages[0]
    }
    return render(request, 'books.html', dict_books)

def booksDetail(request, pk):
    dict_book={
        'book': Books.objects.get(id=pk)
    }
    return render(request, 'book_detail.html', dict_book)

def members(request):
    dict_members={
        'members': Members.objects.all()
    }
    return render(request, 'members.html', dict_members)

def transactions(request):
    dict_transactions={
        'transactions': Transactions.objects.all()
    }
    return render(request, 'transactions.html', dict_transactions)

# CRUD for Books Model
def newBooks(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    context = {'form':form}
    return render(request, 'book_form.html', context)

def updateBooks(request, pk):
    book = Books.objects.get(id=pk)
    form = BooksForm(instance=book)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    context = {'form':form}
    return render(request, 'book_form.html', context)

def deleteBooks(request, pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/books/')
    context = {'item':book}
    return render(request, 'delete_books.html', context)

# CRUD for Members Model
def newMembers(request):
    form = MembersForm()
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members/')
    context = {'form':form}
    return render(request, 'members_form.html', context)

def updateMembers(request, pk):
    member = Members.objects.get(id=pk)
    form = MembersForm(instance=member)
    if request.method == 'POST':
        form = MembersForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/members/')
    context = {'form':form}
    return render(request, 'members_form.html', context)

def deleteMembers(request, pk):
    member = Members.objects.get(id=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('/members/')
    context = {'item':member}
    return render(request, 'delete_members.html', context)

# Pagination
def pagination(request, list, num):
    paginator = Paginator(list, num)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number-1
    max_index = len(paginator.page_range)
    start_index = index-2 if index >= 2 else 0
    end_index = index+2 if index <= max_index-2 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return items, page_range

# Search a Book
def searchBooks(request):
    query = []
    query = request.GET.get('q')
    if query:
        results = Books.objects.filter(Q(title__icontains=query) | Q(authors__icontains=query))
    else:
        results = Books.objects.all()
    pages = pagination(request, results, num=20)
    context = {
        'books': pages[0],
        'page_range' : pages[1],
        'query' : query
    }
    return render(request, 'books.html', context)

#Issue a Book
def newTransactions(request, pk):
    book = Books.objects.get(id=pk)
    form = TransactionsForm(initial={'book_id':book})
    if request.method == 'POST':
        form = TransactionsForm(request.POST)
        if form.is_valid():
            trans_instance = form.save()
            book.transactions_ids = trans_instance
            book.availability = False
            book.status = 'Issued'
            book.save(update_fields=['availability', 'status', 'transactions_ids'])
            # outstanding fee calculation
            return redirect('/transactions/')
    context = {'form':form, 'action':'issue'}
    return render(request, 'transactions_form.html', context)

#Return a Book
def returnBooks(request, pk):
    book = Books.objects.get(id=pk)
    if book.transactions_ids:
        transaction = Transactions.objects.get(id=book.transactions_ids.id)
        form = TransactionsForm(instance=transaction)
        if request.method == 'POST':
            form = TransactionsForm(request.POST, instance=transaction)
            if form.is_valid():
                    form.save()
                    fees = 0
                    transaction = Transactions.objects.get(id=book.transactions_ids.id)
                    member = book.transactions_ids.member_id
                    for t in Transactions.objects.all():
                        if t.member_id == member:
                            fees = fees + int(t.fees)
                    if fees > 500:
                        context = {
                            'warning' : True,
                            'warningmsg':"Outstanding fees of Rs." + str(fees)
                        }
                        return render(request, 'transactions_form.html', context)
                    book.availability = True
                    book.status = 'Returned'
                    book.save(update_fields=['availability', 'status'])
                    return redirect('/transactions/')
        context = {'form':form}
        return render(request, 'transactions_form.html', context)
    else:
        return redirect('/books/')
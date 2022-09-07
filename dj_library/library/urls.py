from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library'),

    # path('register/', views.registerPage, name='register'),
    # path('login/', views.loginPage, name='login'),
    # path('logout/', views.logoutUser, name='logout'),

    path('books/', views.books, name='books'),
    path('booksdetail/<str:pk>/', views.booksDetail, name='book_detail'),

    path('members/', views.members, name='members'),

    path('transactions/', views.transactions, name='transactions'),

    path('newbooks/', views.newBooks, name='new_books'),
    path('updatebooks/<str:pk>/', views.updateBooks, name='update_books'),
    path('deletebooks/<str:pk>/', views.deleteBooks, name='delete_books'),

    path('newmembers/', views.newMembers, name='new_members'),
    path('updatemembers/<str:pk>/', views.updateMembers, name='update_members'),
    path('deletemembers/<str:pk>/', views.deleteMembers, name='delete_members'),

    path('newtransactions/<str:pk>/', views.newTransactions, name='new_transactions'),
    path('returnbooks/<str:pk>/', views.returnBooks, name='return_books'),
    path('searchbooks/', views.searchBooks, name='search_books'),
]

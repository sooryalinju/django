from django.contrib import admin
from .models import Books, Members, Transactions

# Register your models here.
@admin.register(Books)
class Books(admin.ModelAdmin):
    list_display = ( 'title', 'authors', 'isbn', 'num_pages', 'publisher')
    list_filter = ('title', 'authors')

class TransactionsInline(admin.TabularInline):
    model = Transactions
    extra = 0

@admin.register(Members)
class Members(admin.ModelAdmin):
    list_display = ('memberID', 'name')
    inlines = [TransactionsInline]
    fields = ['memberID', 'name']

@admin.register(Transactions)
class Transactions(admin.ModelAdmin):
    list_display = ('name', 'member_id', 'book_id','due_date','fees')


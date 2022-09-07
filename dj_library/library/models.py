from django.db import models
from django.db.models import Model

# Create your models here.
class Books(models.Model):
    bookID = models.CharField('Book ID', max_length=100)
    title = models.CharField('Title', max_length=100)
    authors = models.CharField('Authors', max_length=200)
    average_rating = models.DecimalField('Average Rating', max_digits=10, decimal_places=5)
    isbn = models.CharField('ISBN', max_length=100)
    isbn13 = models.CharField('ISBN13', max_length=100)
    language_code = models.CharField('Language Code', max_length=10)
    num_pages = models.IntegerField('Pages')
    ratings_count = models.IntegerField('Ratings')
    text_reviews_count = models.IntegerField('Text Review Counts')
    publication_date = models.DateField('Publication Date', null=True, blank=True)
    publisher = models.CharField('Publisher', max_length=100)
    availability = models.BooleanField('Availability', null=True, default=True)
    STATUS = (('Issued', 'Issued'), ('Returned', 'Returned'))
    status = models.CharField(max_length=100, choices=STATUS, blank=True, default='Returned',
                                help_text='Staus')
    transactions_ids = models.ForeignKey('Transactions', related_name='book_transactions', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Members(models.Model):
    name = models.CharField('Name', max_length=100)
    memberID = models.CharField('Member ID', max_length=100)
    transactions_ids = models.ForeignKey('Transactions', related_name='member_transactions', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Transactions(models.Model):
    name = models.CharField('Transaction No.', max_length=100, null=True, blank=True)
    book_id = models.ForeignKey('Books', on_delete=models.CASCADE, null=True, blank=True)
    member_id = models.ForeignKey('Members', on_delete=models.CASCADE, null=True, blank=True)
    borrowed_date = models.DateField('Borrowed Date', null=True, blank=True)
    due_date = models.DateField('Due Date', null=True, blank=True)
    fees = models.CharField('Fees', max_length=100, null=True, blank=True, default=0)

    def __str__(self):
        return self.name
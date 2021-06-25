from rest_framework import serializers

from books.models import Book

class BookCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=Book
		fields=('title','subtitle','isbn')


class BookListSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='author.username')
	class Meta:
		model=Book
		fields=('id','title','subtitle','username','isbn')

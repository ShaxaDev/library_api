from django.shortcuts import render


from rest_framework import generics
from rest_framework.permissions import (
		AllowAny,
		IsAdminUser,
		IsAuthenticated,
		IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
)
from .my_filters import IsOwnerFilterBackend

from books.models import Book
from .serializers import BookListSerializer,BookCreateSerializer

class BookLISTAPIView(generics.ListAPIView):
	queryset=Book.objects.all()
	serializer_class = BookListSerializer
	permission_classes=[IsAuthenticated]
	filter_backends = [SearchFilter,OrderingFilter,IsOwnerFilterBackend]
	search_fields=['title','author__username','subtitle']



class BookDetailView(generics.RetrieveAPIView):
	queryset=Book.objects.all()
	serializer_class=BookListSerializer


class BookUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookCreateSerializer
	permission_classes=[IsOwnerOrReadOnly]

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)

class BookDeleteAPIView(generics.DestroyAPIView):
	queryset=Book.objects.all()
	serializer_class=BookListSerializer

class BookCreateAPIView(generics.CreateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookCreateSerializer

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)

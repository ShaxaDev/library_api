from django.urls import path
from .views import (BookLISTAPIView,BookDetailView,
					BookCreateAPIView,BookDeleteAPIView,
					BookUpdateAPIView)


urlpatterns = [
	path('', BookLISTAPIView.as_view(), name='home'),
	path('create/',BookCreateAPIView.as_view(),name='create'),
	path('<int:pk>/',BookDetailView.as_view(),name='detail'),
	path('<int:pk>/delete/',BookDeleteAPIView.as_view(),name='delete'),
	path('<int:pk>/edit/',BookUpdateAPIView.as_view(),name='update'),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet, BookListView, BooklistUpdateDelete

# router = DefaultRouter()
# router.register(r'books', BookViewSet, basename="book")

# urlpatterns = [
#     path('', include(router.urls)),
#     path('books/list/', BookListView.as_view()),
#     path('books/<int:pk>/', BooklistUpdateDelete.as_view()),
    
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="book")

urlpatterns = [
    # path('', include(router.urls)),
    # path('books/list/', BookListCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('', include(router.urls)),

]


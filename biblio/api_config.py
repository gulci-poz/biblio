from rest_framework import routers

from shelf.api import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

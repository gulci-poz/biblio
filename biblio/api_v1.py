from rest_framework import routers

from shelf.api import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

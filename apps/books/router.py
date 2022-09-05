from rest_framework.routers import SimpleRouter
from apps.books.viewsets import PublishingHouseAction

router = SimpleRouter()

router.register(r'publishing_house', PublishingHouseAction, basename='PublishingHouse')

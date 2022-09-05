# from django.urls import path
# from apps.books.viewsets import PublishingHouseAction, DetailPublishingHouseAction
#
# urlpatterns = [
#     path('publishing_house/', PublishingHouseAction.as_view()),
#     path('publishing_house/<int:pk>', DetailPublishingHouseAction.as_view()),
# ]
from apps.books.router import router as book_router

urlpatterns = book_router.urls
# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
# from rest_framework.mixins import CreateModelMixin
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.books.models import PublishingHouse
from apps.books.serializers import PublishingHouseSerializer


class PublishingHouseAction(ViewSet):
    def list(self, request):
        quaryset = PublishingHouse.objects.all()
        serrializer = PublishingHouseSerializer(quaryset, many=True)
        return Response(serrializer.data)

    def create(self, request, pk):
        quaryset = PublishingHouse.objects.all()
        handler = get_object_or_404(quaryset, pk=pk)
        serrializer = PublishingHouseSerializer(handler, many=True)
        return Response(serrializer.data)



# class PublishingHouseAction(CreateModelMixin, ListAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer
#
#
# class DetailPublishingHouseAction(RetrieveUpdateDestroyAPIView):
#     queryset = PublishingHouse.objects.all()
#     serializer_class = PublishingHouseSerializer

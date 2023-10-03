from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from storage.models import File
from storage.serializers import FileSerializer
from storage.tasks import process_file


@api_view(["POST"])
def upload(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        file = serializer.save()
        process_file.delay(file.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

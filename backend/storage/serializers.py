from django.forms import ValidationError
from rest_framework import serializers

from storage.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("id", "file", "uploaded_at", "processed")
        read_only_fields = ("id", "uploaded_at", "processed")

    def validate_file(self, value):
        ext = value.name.split(".")[-1]
        if ext not in ["jpg", "jpeg", "png", "txt", "pdf"]:
            raise ValidationError("Неподдерживаемое расширение файла.")
        return value

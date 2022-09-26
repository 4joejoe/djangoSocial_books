from rest_framework import serializers

class book_serializer(serializers.Serializer):
    BookName = serializers.CharField(max_length=50)
    AuthorName = serializers.CharField(max_length=50)
    file = serializers.FileField()
from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

## 11:20~
class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'image', 'desc', 'author_name')

class FilesSerializer(serializers.ModelSerializer):

    ###
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)
    

    class Meta:
        model = Files
        fields = ('pk', 'myfile', 'desc', 'author')
    ###
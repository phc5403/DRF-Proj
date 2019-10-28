from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter

# file_uploading : Paser
from rest_framework.parsers import MultiPartParser, FormParser

# def post()
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):

    # 각각 Model, Serializer 필요
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body') # 반드시 튜플로!

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self): # +admin만 모든 user글 다 보이게 해보기
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs

class ImgViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    # 다양한 미디어타입으로 Request를 수락하는 방법들 중 하나
    parser_classes = (MultiPartParser, FormParser)

    # paser_class 지정
    # create() 오버라이딩(APIView에서의 create() -> post())

    def post(self, reqeust, *args, **kwargs):
        serializer = FilesSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
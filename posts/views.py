from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer


class ListPosts(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        return Response(PostSerializer(queryset, many=True).data)

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import *
from .pagination import PostPageNumberPagination


# Create your views here.

class HomeView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')[:7]
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ArticleView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination


class CommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AboutView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AuthorSerializer

from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

@method_decorator(ensure_csrf_cookie, name='dispatch')
@method_decorator(login_required, name='dispatch')
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
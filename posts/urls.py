from .views import ListPosts
from django.urls import path

urlpatterns = [
    path('/', ListPosts.as_view())
]

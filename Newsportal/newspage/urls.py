from django.urls import path
from .views import PostList, PostText, PostSearch, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostText.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('add/', PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

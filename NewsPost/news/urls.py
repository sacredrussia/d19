from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, ResponseCreate, ResponseUpdate, NewsCreate, \
    NewsDetail, NewsList

urlpatterns = [
    path('', PostsList.as_view(),  name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/res_create/', ResponseCreate.as_view(), name='response_create'),
    path('<int:pk>/res_update/', ResponseUpdate.as_view(), name='response_update'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/', NewsList.as_view(), name='news_list'),
]

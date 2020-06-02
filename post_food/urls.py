
from django.contrib import admin
from django.urls import path

from .import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,CategaryPostLisView

urlpatterns = [
    path('h/',PostListView.as_view(),name='home'),
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blogs'),
    path('post/<int:id>/',views.post,name='post-details'),
   # path('post/<int:pk>/',PostDetailView.as_view(),name='post-details'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    #
    path('post/Cat/<int:id>/', CategaryPostLisView.as_view(), name='cat-posts'),

    path('create/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('test/',views.test,name='test'),
]

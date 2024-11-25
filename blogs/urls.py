from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.PostListView.as_view(), name='postlist'),
    path('addpost/', views.AddPostView.as_view() , name='addpost'),
    path('users/', views.UserSearch.as_view(), name='users'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', views.PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', views.CommentReplyView.as_view(), name='comment-reply'),
    path('post/<int:pk>/like', views.AddLike.as_view(), name='like'),
    
] 

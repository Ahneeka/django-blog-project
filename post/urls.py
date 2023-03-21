from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name='hello'),
    path("greet/", views.greet, name='greet'),
    path("greeting/", views.greeting, name='greeting'),
    # path("", views.home, name='home'),
    path("", views.PostListView.as_view(), name='home'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('post/new/', views.PostCreateView.as_view(), name='new_post'),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
]


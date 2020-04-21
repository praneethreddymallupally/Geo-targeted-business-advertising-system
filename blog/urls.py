from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserProfileView,UserPostListView
urlpatterns = [
    path('displayadd/',views.displayadd,name="add"),
    path('bid/payment/',views.payment,name="payment"),
    path('publisher',views.publisher,name="publisher"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('bid/',views.bid,name="bid"),
    path('profile/<int:pk>/',UserProfileView.as_view(),name="user-detail"),
]



#<app>/<model>_<viewtype>.html


        
        

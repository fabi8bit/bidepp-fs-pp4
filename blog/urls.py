from . import views
from blog.views import index_home
from django.urls import path


urlpatterns = [
    path('', index_home, name='home'),
    path('blog/', views.ReviewList.as_view(), name='blog'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]
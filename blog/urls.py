from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]
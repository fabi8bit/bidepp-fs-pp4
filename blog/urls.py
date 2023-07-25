from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexHome.as_view(), name='home'),
    path('blog/', views.ReviewList.as_view(), name='blog'),
    path('map/', views.HotelList.as_view(), name='map'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]
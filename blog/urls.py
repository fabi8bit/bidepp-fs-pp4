from . import views
from django.urls import path
from django.conf.urls import url
from .views import review_form


urlpatterns = [
    path('', views.IndexHome.as_view(), name='home'),
    path('form/', views.review_form, name='review_form'),
    path('blog/', views.ReviewList.as_view(), name='blog'),
    path('map/', views.HotelList.as_view(), name='map'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]

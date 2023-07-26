from . import views
from django.urls import path
from django.conf.urls import url
from .views import review_form


urlpatterns = [
    path('', views.IndexHome.as_view(), name='home'),
    # insert new Review
    path('form/', views.review_form, name='review_form'),
    # update Review
    path('form/<slug:slug>/', views.review_form, name='review_update'),
    # delete Hotel
    path('delete/<int:id>/', views.hotel_delete, name='hotel_delete'),
    # delete Review
    path('delete/<slug:slug>/', views.review_delete, name='review_delete'),
    # insert new Hotel
    path('hotelform/', views.hotel_form, name='hotel_form'),
    # update Hotel
    path('hotelform/<int:id>/', views.hotel_form, name='hotel_update'),
    path('list/', views.ReviewList.as_view(
        template_name='review_list.html'), name='review_list'),
    path('blog/', views.ReviewList.as_view(
        template_name='blog.html', paginate_by=6), name='blog'),
    path('map/', views.HotelList.as_view(), name='map'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]

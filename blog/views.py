from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6





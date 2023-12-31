from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review, Hotel
from .forms import CommentForm, CreateReviewForm, CreateHotelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = Review.objects.filter(status=1).order_by(
            '-created_on')
        context['navbar'] = 'blog'
        return context


class ManageList(UserPassesTestMixin, generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = Review.objects.filter(status=1).order_by(
            '-created_on')
        context['navbar'] = 'manage'
        return context


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        invalid_form = False

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
            messages.add_message(request, messages.INFO, 'Comment submitted')
        else:
            invalid_form = True
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
                "invalid_form": invalid_form
            },
        )


class ReviewLike(View):
    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))


class HotelDetail(View):

    def get(self, request, id, *args, **kwargs):
        queryset = Hotel.objects.all()
        hotel = get_object_or_404(queryset, pk=id)
        reviews = hotel.blog_reviews.filter(
            status=1).order_by('-created_on')

        return render(
            request,
            "hotel_detail.html",
            {
                "hotel": hotel,
                "reviews": reviews
            },
        )


class IndexHome(generic.ListView):
    model = Hotel
    queryset = Hotel.objects.order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'home'

        return context


class HotelList(generic.ListView):
    model = Hotel
    queryset = Hotel.objects.order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'hotels'

        return context


def review_form(request, slug=""):
    if request.method == "GET":
        if slug == "":
            form = CreateReviewForm()
        else:
            review = Review.objects.get(slug=slug)
            form = CreateReviewForm(instance=review)
        return render(request, "review_form.html", {'form': form})
    else:
        if slug == "":
            # solution from here:
            # https://stackoverflow.com/questions/59663492/django-form-successful-but-image-not-uploaded
            form = CreateReviewForm(request.POST, request.FILES or None)
        else:
            review = Review.objects.get(slug=slug)
            form = CreateReviewForm(
                request.POST, request.FILES or None, instance=review)
        if form.is_valid():
            check = form.save(commit=False)
            check.user = request.user
            check.save()
        return redirect('/list/')


def review_delete(request, slug):
    review = get_object_or_404(Review, slug=slug)
    review.delete()
    return redirect('/list/')


def hotel_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CreateHotelForm()
        else:
            hotel = Hotel.objects.get(pk=id)
            form = CreateHotelForm(instance=hotel)
        return render(request, "hotel_form.html", {'form': form})
    else:
        if id == 0:
            form = CreateHotelForm(request.POST, request.FILES or None)
        else:
            hotel = Hotel.objects.get(pk=id)
            form = CreateHotelForm(
                request.POST, request.FILES or None, instance=hotel)
        if form.is_valid():
            check = form.save(commit=False)
            check.user = request.user
            check.save()
        return redirect('/list/')


def hotel_delete(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    hotel.delete()
    return redirect('/list/')


def search_hotels(request):

    if request.method == "POST":
        searched = request.POST['searched']
        hotels = Hotel.objects.filter(country__icontains=searched)
        return render(request, "search_hotels.html", {
            'searched': searched,
            'hotels': hotels
            })
    else:
        return render(request, "hotels.html", {})

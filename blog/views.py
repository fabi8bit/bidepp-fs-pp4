from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review, Hotel
from .forms import CommentForm, CreateReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


# def index_home(request):
#     return render(request, 'index.html')  

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    # template_name = 'blog.html'
    paginate_by = 6


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


class IndexHome(generic.ListView):
    model = Hotel
    queryset = Hotel.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class HotelList(generic.ListView):
    model = Hotel
    queryset = Hotel.objects.order_by('-created_on')
    template_name = 'map.html'
    paginate_by = 6


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
        if slug == "":
            return redirect('/blog/')
        else:
            return redirect('/list/')
        
            
def review_delete(request, slug):
    review = get_object_or_404(Review, slug=slug)
    review.delete()
    return redirect('/list/')

# def review_list(request):
#     context = {'review_list': }
#     return render(request, "review_list.html")



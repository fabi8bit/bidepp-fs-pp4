from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment:',
        }


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    # this method initialize the list of the dropdown menu
    # and replace the empty label "----" with "Select"
    # taken from this tutorial https://www.youtube.com/watch?v=N6jzspc2kds&t=3387s

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields['hotel'].empty_label = "Select"
        self.fields['author'].empty_label = "Select"
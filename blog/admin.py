from django.contrib import admin
from .models import Review, Hotel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(Hotel)

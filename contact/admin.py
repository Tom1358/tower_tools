from django.contrib import admin

from .models import Feedback

class FeedbackForm(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'date',
        'summary',
        'your_message',
    )

    ordering = ('full_name',)


admin.site.register(Feedback, FeedbackForm)


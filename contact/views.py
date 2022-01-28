from django.shortcuts import render

from .forms import FeedbackForm
from profiles.models import UserProfile


def feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'contact/thanks.html')
    else:
        form = FeedbackForm()

    return render(request, 'contact/feedback_form.html', {'form': form})
    

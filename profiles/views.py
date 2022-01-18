from django.shortcuts import render


def profile(request):
    """ display profile """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
    
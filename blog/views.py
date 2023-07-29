from django.shortcuts import render


def blog(request):
    """ A view to return the index page """

    return render(request, 'blog.html')

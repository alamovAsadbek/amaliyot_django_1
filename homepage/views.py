from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Welcome to the homepage!")

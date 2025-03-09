from django.http import HttpResponse

# Simple home view for testing
def home(request):
    return HttpResponse("Welcome to the Depression Detection App!")

# Simple about page
def about(request):
    return HttpResponse("This is the about page of the Depression Detection App.")
